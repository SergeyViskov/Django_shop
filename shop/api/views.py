from rest_framework.response import Response
from rest_framework.decorators import api_view

from goods.models import SuperCategory, Goods
from .serializers import SuperCategorySerializer, GoodsSerializes, GoodsDetailSerializes

@api_view(['GET'])
def super_category(request):
    if request.method == 'GET':
        super_category = SuperCategory.objects.all()
        serializer = SuperCategorySerializer(super_category, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def goods(request):
    if request.method == 'GET':
        goods = Goods.objects.all()
        serializer = GoodsSerializes(goods, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def goods_detail(request, id):
    if request.method == 'GET':
        goods = Goods.objects.filter(id=id)
        serializer = GoodsDetailSerializes(goods, many=True)
        return Response(serializer.data)
