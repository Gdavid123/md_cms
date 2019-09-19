from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ReadOnlyModelViewSet

from meiduo_admin.serializer.orders import OrderListSerializer, OrderDetailSerializer, OrderStatusSerializer
from orders.models import OrderInfo


class OrdersViewSet(UpdateModelMixin,ReadOnlyModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = OrderListSerializer

    # list操作和retrieve操作使用的序列化器类不同，所以这里重写get_serializer_class方法。
    def get_serializer_class(self):
        """返回视图所使用的序列化器类"""
        if self.action == 'list':
            return OrderListSerializer
        elif self.action == 'retrieve':
            return OrderDetailSerializer
        else:
            return OrderStatusSerializer

    def get_queryset(self):
        keyword = self.request.query_params.get('keyword')
        if not keyword:
            orders = OrderInfo.objects.all()
        else:
            orders = OrderInfo.objects.filter(Q(order_id=keyword) |Q(skus__sku__name__contains=keyword))

        return orders


    @action(methods=['put'],detail=True)
    def status(self,request,pk):
        return self.update(request,pk)
