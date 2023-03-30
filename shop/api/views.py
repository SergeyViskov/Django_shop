from rest_framework.response import Response
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from goods.models import SuperCategory, Goods
from .serializers import (
    SuperCategorySerializer,
    GoodsSerializes,
    GoodsDetailSerializes,
)
from .pagination import LimitPagination


class SuperCategoriesView(ListAPIView):
    queryset = SuperCategory.objects.all()
    serializer_class = SuperCategorySerializer
    pagination_class = LimitPagination


class GoodsView(ListAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializes
    pagination_class = LimitPagination


class GoodsDetailView(APIView):
    def get(self, request, id):
        goods = get_list_or_404(Goods, id=id)
        serializer = GoodsDetailSerializes(goods, many=True)
        return Response(serializer.data)
