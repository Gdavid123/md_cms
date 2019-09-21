import json

from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from goods.models import SPU, SPUSpecification, Brand, GoodsCategory, SpecificationOption
from meiduo_admin.serializer.spus import SPUSimpleSerializer, SPUSpecSerializer, SPUSerializer, BrandSerializer, \
    FCategoriesSerializer, SubCategoriesSerializer, GoodsSpecsSerializer, SpecsOptionSerializer, SpecsSimpleSerializer, \
    GoodsBrandSerializer
from settings.dev import FDFS_URL
from utils.fdfs.storage import FDFSStorage
from django.conf import settings

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






class SPUViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = SPUSerializer
    queryset = SPU.objects.all()
    client_conf = settings.FDFS_CLIENT_CONF

    @action(methods=['post'],detail=False)
    def images(self, request):
        img = request.data.get('image')
        file_id = FDFSStorage._save(self, name='', content=img)
        image_url = FDFS_URL + file_id
        data = {
            'img_url':image_url

        }
        return Response(data)





class SPUBrandsSimple(ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    pagination_class = None



class SPUCategoriesSimple(ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = FCategoriesSerializer
    queryset = GoodsCategory.objects.filter(parent=None)
    pagination_class = None


class SPUSubCategoriesSimple(APIView):
    permission_classes = [IsAdminUser]
    serializer_class = SubCategoriesSerializer
    pagination_class = None
    def get(self,request,pk):
        obj = GoodsCategory.objects.get(id=pk)
        serializer = SubCategoriesSerializer(obj)
        return Response(serializer.data)




class GoodsSpecsViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = GoodsSpecsSerializer
    queryset = SPUSpecification.objects.all()



class SpecsOptionsViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = SpecsOptionSerializer
    queryset = SpecificationOption.objects.all()


class SpecsSimple(ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = SpecsSimpleSerializer
    queryset = SPUSpecification.objects.all()
    pagination_class = None


class GoodsBrandViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = GoodsBrandSerializer
    queryset = Brand.objects.all()
