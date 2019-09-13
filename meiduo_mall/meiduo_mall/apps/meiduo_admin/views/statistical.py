# GET /meiduo_admin/statistical/total_count/
from django.utils import timezone
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from goods.models import GoodsVisitCount
from meiduo_admin.serializer.statistical import GoodsVisitSerializer
from users.models import User

# GET /meiduo_admin/statistical/total_count/
class UserTotalCountView(APIView):
    permission_classes = [IsAdminUser]

    def get(self,request):
        """
        获取网站总用户数
        :param request:
        :return:
        """

        now_date = timezone.now()
        count = User.objects.count()

        response_data = {
            # timezone.now().data()只返回`年-月-日`
            'date':now_date.date(),
            'count':count
        }

        return Response(response_data)



# GET /meiduo_admin/statistical/day_increment/
class UserDayIncrementView(APIView):
    permission_classes = [IsAdminUser]

    def get(self,request):
        """
        获取日增用户数量
        :param request:
        :return:
        """

        now_date = timezone.now().replace(hour=0,minute=0,second=0,microsecond=0)
        count = User.objects.filter(date_joined__gte=now_date).count()

        response_data = {
            'data':now_date.date(),
            'count':count
        }

        return Response(response_data)



# GET /meiduo_admin/statistical/day_active/
class UserDayActiveView(APIView):
    permission_classes = [IsAdminUser]

    def get(self,request):
        """
        获取日活用户量
        :param request:
        :return:
        """
        now_date = timezone.now().replace(hour=0,minute=0,second=0,microsecond=0)
        count = User.objects.filter(last_login__gte=now_date).count()

        response_data = {
            'data':now_date.date(),
            'count':count
        }

        return Response(response_data)


# GET /meiduo_admin/statistical/day_orders/
class UserDayOrdersView(APIView):
    permission_classes = [IsAdminUser]

    def get(self,request):
        """
        获取日下单用户数量
        :param request:
        :return:
        """

        now_date = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        count = User.objects.filter(orders__create_time__gte=now_date).distinct().count()

        response_data = {
            'date':now_date.date(),
            'count':count
        }

        return Response(response_data)



# GET /meiduo_admin/statistical/month_increment/
class UserMonthCountView(APIView):
    permission_classes = [IsAdminUser]

    def get(self,request):
        # 结束时间
        now_date = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)

        # 起始时间
        begin_date = now_date - timezone.timedelta(days=29)

        # 当天日期
        current_date = begin_date

        # 30天每天新增用户数量
        month_li = []

        while current_date <= now_date:
            # 次日时间
            next_date = current_date + timezone.timedelta(days=1)

            # 统计当天的新增用户数量
            count = User.objects.filter(date_joined__gte=current_date,
                                        date_joined__lt=next_date).count()

            month_li.append({
                'count':count,
                'date':current_date.date()
            })

            current_date += timezone.timedelta(days=1)

        return Response(month_li)



# GET /meiduo_admin/statistical/goods_day_views/
class GoodsDayView(APIView):
    permission_classes = [IsAdminUser]

    def get(self,request):
        """
        获取当日分类商品访问量
        :param request:
        :return:
        """
        now_date = timezone.now().date()

        goods_visit = GoodsVisitCount.objects.filter(date=now_date)

        serializer = GoodsVisitSerializer(goods_visit,many=True)

        return Response(serializer.data)
