from rest_framework import serializers

from goods.models import SPU, SpecificationOption, SPUSpecification


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
