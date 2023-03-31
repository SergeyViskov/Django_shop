from rest_framework.response import Response
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from goods.models import SuperCategory, Goods, Cart, CartItems
from .serializers import (
    SuperCategorySerializer,
    GoodsSerializes,
    GoodsDetailSerializes,
    CartItemsSerialiser,
)
from .pagination import LimitPagination
from .permissions import IsReadOnly


class SuperCategoriesView(ListAPIView):
    permission_classes = [IsReadOnly]
    queryset = SuperCategory.objects.all()
    serializer_class = SuperCategorySerializer
    pagination_class = LimitPagination


class GoodsView(ListAPIView):
    permission_classes = [IsReadOnly]
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializes
    pagination_class = LimitPagination


class GoodsDetailView(APIView):
    permission_classes = [IsReadOnly]
    def get(self, request, id):
        goods = get_list_or_404(Goods, id=id)
        serializer = GoodsDetailSerializes(goods, many=True)
        return Response(serializer.data)


class CartView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        cart = Cart.objects.filter(user=user, ordered=False).first()
        queryset = CartItems.objects.filter(cart=cart)
        serialiser = CartItemsSerialiser(queryset, many=True)
        return Response(serialiser.data)

    def post(self, request):
        data = request.data
        user = request.user
        cart,_ = Cart.objects.get_or_create(user=user, ordered=False)
        goods = Goods.objects.get(id=data.get('goods'))
        price = goods.price
        quantity = data.get('quantity')
        cart_items = CartItems(cart=cart, user=user, goods=goods, price=price, quantity=quantity)
        cart_items.save()
        total_price = 0
        cart_items = CartItems.objects.filter(user=user, cart=cart.id)
        for items in cart_items:
            total_price += items.price
        cart.total_price = total_price
        cart.save()
        return Response({'success': 'Items added to your cart'})

    def put(self, request):
        data = request.data
        cart_items = CartItems.objects.get(id=data.get('id'))
        quantity = data.get('quantity')
        cart_items.quantity += quantity
        cart_items.save()
        return Response({'success': 'Items updated'})
    
    def delete(self, request):
        user = request.user
        data = request.data
        cart_items = CartItems.objects.filter(id=data.get('id'))
        cart_items.delete()
        cart = Cart.objects.filter(user=user, ordered=False).first()
        queryset = CartItems.objects.filter(cart=cart)
        serialiser = CartItemsSerialiser(queryset, many=True)
        return Response(serialiser.data)
