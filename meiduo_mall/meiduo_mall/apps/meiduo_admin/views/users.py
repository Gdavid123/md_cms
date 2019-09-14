from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from meiduo_admin.serializer.users import AdminAuthSerializer, UserSerializer
# from rest_framework.generics import CreateAPIView
# POST /meiduo_admin/authorizations/
from users.models import User


class AdminAuthorizeView(APIView):
    def post(self, request):
        """
        管理员登录:
        1. 获取参数并进行校验
        2. 服务器签发jwt token数据
        3. 返回应答
        """
        # 1. 获取参数并进行校验
        serializer = AdminAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 2. 服务器签发jwt token数据(create)
        serializer.save()

        # 3. 返回应答
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# GET /meiduo_admin/users/?keyword=<搜索内容>&page=<页码>&pagesize=<页容量>
class UserInfoView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    # 指定视图所使用的序列化器类
    serializer_class = UserSerializer

    def get_queryset(self):
        """返回视图所使用的查询集"""
        # 1. 获取keyword关键字
        keyword = self.request.query_params.get('keyword')

        # 2. 查询普通用户数据
        if keyword:
            users = User.objects.filter(is_staff=False, username__contains=keyword)
        else:
            users = User.objects.filter(is_staff=False)

        return users

