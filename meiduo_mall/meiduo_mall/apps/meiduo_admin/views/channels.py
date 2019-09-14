# GET /meiduo_admin/goods/channels/?page=<页码>&page_size=<页容量>
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from goods.models import GoodsChannel, GoodsChannelGroup, GoodsCategory
from meiduo_admin.serializer.channels import ChannelSerializer, ChannelGroupSerializer, ChannelCategorySerializer


class ChannelViewSet(ModelViewSet):
    """频道管理视图集"""
    permission_classes = [IsAdminUser]
    queryset = GoodsChannel.objects.all()
    serializer_class = ChannelSerializer



class ChannelTypesView(ListAPIView):
    """频道组视图"""
    permission_classes = [IsAdminUser]
    queryset = GoodsChannelGroup.objects.all()
    serializer_class = ChannelGroupSerializer
    pagination_class = None



class ChannelCategoriesView(ListAPIView):
    """频道对应一级分类视图"""
    permission_classes = [IsAdminUser]
    queryset = GoodsCategory.objects.filter(parent=None)
    serializer_class = ChannelCategorySerializer
    pagination_class = None
