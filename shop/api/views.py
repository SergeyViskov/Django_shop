from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView

from goods.models import SuperCategory, Goods
from .serializers import SuperCategorySerializer, GoodsSerializes, GoodsDetailSerializes


class SuperCategoriesView(APIView):
    def get(self, request):
        super_category = SuperCategory.objects.all()
        serializer = SuperCategorySerializer(super_category, many=True)
        return Response(serializer.data)


class GoodsView(APIView):
    def get(self, request):
        goods = Goods.objects.all()
        serializer = GoodsSerializes(goods, many=True)
        return Response(serializer.data)


class GoodsDetailView(APIView):
    def get(self, request, id):
        goods = get_list_or_404(Goods, id=id)
        serializer = GoodsDetailSerializes(goods, many=True)
        return Response(serializer.data)
