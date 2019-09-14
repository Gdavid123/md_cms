from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class StandardResultPagination(PageNumberPagination):
    """自定义分页类"""
    page_size = 5
    page_size_query_param = 'pagesize'
    max_page_size = 20

    def get_paginated_response(self, data):
        """重写父类方法,自定义分页响应数据格式"""
        a = OrderedDict([
            ('counts', self.page.paginator.count),
            ('lists', data),
            ('page', self.page.number),
            ('pages', self.page.paginator.num_pages),
            ('pagesize', self.get_page_size(self.request))
        ])
        return Response(a)
