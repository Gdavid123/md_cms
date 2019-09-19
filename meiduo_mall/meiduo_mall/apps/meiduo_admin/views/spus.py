from rest_framework.decorators import action
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from goods.models import SPU, SPUSpecification, Brand, GoodsCategory
from meiduo_admin.serializer.spus import SPUSimpleSerializer, SPUSpecSerializer, SPUSerializer, BrandSerializer, \
    FCategoriesSerializer, SubCategoriesSerializer

from meiduo_mall.utils.fdfs.storage import FDFSStorage


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

    @action(methods=['post'], detail=False)
    def image(self, request):
        FDFS_URL = 'http://127.0.0.1:8888/'
        file_id = FDFSStorage.save(self, name='', content=request.data)
        image_url = FDFS_URL + file_id
        return Response(image_url)





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


