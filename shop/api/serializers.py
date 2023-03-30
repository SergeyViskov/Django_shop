from rest_framework import serializers

from goods.models import SuperCategory, Goods


class SuperCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperCategory
        fields = (
            'id',
            'name',
            'slug',
        )


class GoodsSerializes(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = (
            'id',
            'title',
            'sub_category',
            'slug',
            'price',
            'image',
        )


class GoodsDetailSerializes(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = (
            'id',
            'title',
            'sub_category',
            'slug',
            'price',
            'image',
        )
