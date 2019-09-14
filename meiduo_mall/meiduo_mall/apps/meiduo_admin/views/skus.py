# GET  /meiduo_admin/skus/images/?page=<页码>&page_size=<页容量>
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from goods.models import SKUImage, SKU
from meiduo_admin.serializer.skus import SKUImageSerializer, SKUSimpleSerializer


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
