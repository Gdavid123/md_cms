# GET  /meiduo_admin/skus/images/?page=<页码>&page_size=<页容量>
from django.db.models import Q
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from goods.models import SKUImage, SKU
from meiduo_admin.serializer.skus import SKUImageSerializer, SKUSimpleSerializer, SKUSerializer


class SKUImageViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = SKUImage.objects.all()
    serializer_class = SKUImageSerializer



# GET /meiduo_admin/skus/simple/
class SKUSimpleView(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = SKU.objects.all()
    serializer_class = SKUSimpleSerializer
    pagination_class = None



class SKUViewSet(ModelViewSet):
    """SKU视图集"""
    permission_classes = [IsAdminUser]
    lookup_value_regex = '\d+'
    serializer_class = SKUSerializer
    def get_queryset(self):
        """获取当前视图所使用的查询集"""
        keyword = self.request.query_params.get('keyword')
        if keyword:
            skus = SKU.objects.filter(Q(name__contains=keyword)|Q(caption__contains=keyword))
        else:
            skus = SKU.objects.all()
        return skus




