from django.urls import path

from .views import super_category, goods, goods_detail


urlpatterns = [
    path('super-category/', super_category),
    path('goods/', goods),
    path('goods/<int:id>/', goods_detail),
]
