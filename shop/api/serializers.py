from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer

from goods.models import SuperCategory, Goods, Cart, CartItems


class SuperCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperCategory
        fields = (
            'id',
            'name',
            'slug',
        )


class GoodsSerializes(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
            ('medium_square_crop', 'crop__400x400'),
            ('small_square_crop', 'crop__50x50')
        ]
    )
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
    image = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
            ('medium_square_crop', 'crop__400x400'),
            ('small_square_crop', 'crop__50x50')
        ]
    )
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


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartItemsSerialiser(serializers.ModelSerializer):
    cart = CartSerializer()
    goods = GoodsSerializes()
    class Meta:
        model = CartItems
        fields = '__all__'
