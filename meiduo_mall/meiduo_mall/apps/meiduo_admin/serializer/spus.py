from rest_framework import serializers

from goods.models import SPU, SpecificationOption, SPUSpecification, Brand, GoodsChannel, GoodsCategory


class SPUSimpleSerializer(serializers.ModelSerializer):
    """SPU序列化器类"""
    class Meta:
        model = SPU
        fields = ('id','name')


class SpecOptionSerializer(serializers.ModelSerializer):
    """SPU规格序列化器类"""
    class Meta:
        model = SpecificationOption
        fields = ('id','value')


class SPUSpecSerializer(serializers.ModelSerializer):
    """SPU序列化器类"""
    options = SpecOptionSerializer(label='Opt选项',many=True)

    class Meta:
        model = SPUSpecification
        fields = ('id','name','options')



class SPUSerializer(serializers.ModelSerializer):
    """SPU"""
    brand = serializers.StringRelatedField(label='品牌名称')
    brand_id = serializers.IntegerField(label='品牌id')
    category1_id = serializers.IntegerField(label='一级分类id')
    category2_id = serializers.IntegerField(label='二级分类id')
    category3_id = serializers.IntegerField(label='三级分类id')

    class Meta:
        model = SPU
        exclude = ('create_time','update_time','category1','category2','category3')


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id','name')


class FCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = ('id','name')


class LastCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = ('id','name')

class SubCategoriesSerializer(serializers.ModelSerializer):
    subs = LastCategoriesSerializer(label='下级分类',many=True)

    class Meta:
        model = GoodsCategory
        fields = ('id','name','subs')



class SPUImageSerializer(serializers.ModelSerializer):
    pass
