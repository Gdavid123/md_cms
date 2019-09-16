from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from goods.models import SPU, SPUSpecification
from meiduo_admin.serializer.spus import SPUSimpleSerializer, SPUSpecSerializer


class SPUSimpleView(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = SPU.objects.all()
    serializer_class = SPUSimpleSerializer
    pagination_class = None



class SPUSpecView(ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = SPUSpecSerializer
    pagination_class = None
    def get_queryset(self):
        pk = self.kwargs['pk']
        return SPUSpecification.objects.filter(spu_id=pk)
    # def get(self,request,pk):
    #     specs = SPUSpecification.objects.filter(spu_id=pk)
    #     serializer= SPUSpecSerializer(specs,many=True)
    #     return Response(serializer.data)
