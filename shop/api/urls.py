from django.urls import path

from .views import (
    SuperCategoriesView,
    SubCategoriesView,
    GoodsView,
    GoodsDetailView,
    CartView,
)


urlpatterns = [
    path('super-category/', SuperCategoriesView.as_view()),
    path('sub-category/', SubCategoriesView.as_view()),
    path('goods/', GoodsView.as_view()),
    path('goods/<int:id>/', GoodsDetailView.as_view()),
    path('cart/', CartView.as_view()),
]
