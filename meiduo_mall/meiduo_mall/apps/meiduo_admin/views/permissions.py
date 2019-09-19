# GET /meiduo_admin/permission/perms/
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from meiduo_admin.serializer.permissions import PermissionSerializer, ContentTypeSerializer, GroupSerializer, \
    PermissionSimpleSerializer, AdminSerializer, GroupSimpleSerializer
from users.models import User


class PermissionViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

    # GET `/meiduo_admin/permission/content_types/`
    def content_types(self, request):
        content_types = ContentType.objects.all()
        serializer = ContentTypeSerializer(content_types,many=True)
        return Response(serializer.data)


# GET  `/meiduo_admin/permission/groups/`
class GroupViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    # GET `/meiduo_admin/permission/simple/`
    def simple(self, request):
        permissions = Permission.objects.all()

        serializer = PermissionSimpleSerializer(permissions,many=True)
        return Response(serializer.data)




class AdminViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = User.objects.filter(is_staff=True)
    serializer_class = AdminSerializer

    # GET /meiduo_admin/permission/groups/simple/
    def simple(self,request):
        """获取用户组数据"""
        groups = Group.objects.all()
        serializer = GroupSimpleSerializer(groups,many=True)
        return Response(serializer.data)
