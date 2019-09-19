from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from users.models import User


class PermissionSerializer(serializers.ModelSerializer):
    """权限序列化器类"""
    class Meta:
        model = Permission
        fields = '__all__'


class ContentTypeSerializer(serializers.ModelSerializer):
    """权限内容类型序列化器类"""
    class Meta:
        model = ContentType
        fields = ('id','name')



class GroupSerializer(serializers.ModelSerializer):
    """用户组序列化器类"""
    class Meta:
        model = Group
        fields = '__all__'


class PermissionSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('id','name')



class AdminSerializer(serializers.ModelSerializer):
    """管理员用户序列化器类"""
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'mobile', 'user_permissions', 'groups','password')
        extra_kwargs = {
            'password':{
                'write_only':True,
                'required':False,
                'allow_blank':True
            }
        }

    def create(self, validated_data):
        """创建管理员用户"""
        # 设置管理员标记is_staff为True
        validated_data['is_staff'] = True
        # print("validated_data:",validated_data)

        # 创建新的管理员用户
        user = super().create(validated_data)
        # print("user",user)

        # 密码加密保存
        password = validated_data['password']
        # print("password",password)
        if not password:
            # 管理员默认密码
            password = '123abc'

        user.set_password(password)
        user.save()
        # print("user.password:",user.password)

        return user

    def update(self, instance, validated_data):
        """修改管理员用户"""
        # 从validated_data中去除密码password  这里pop掉密码 是方便后面修改密码时为密码加密,如果不pop掉 存进数据库的密码是不加密的
        password = validated_data.pop('password',None)

        # 修改管理员账户信息
        super().update(instance,validated_data)

        #修改密码
        if password:
            instance.set_password(password)
            instance.save()

        return instance

class GroupSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')


