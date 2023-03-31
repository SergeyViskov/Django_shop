from django.urls import path

from .views import SuperCategoriesView, GoodsView, GoodsDetailView, CartView


urlpatterns = [
    path('super-category/', SuperCategoriesView.as_view()),
    path('goods/', GoodsView.as_view()),
    path('goods/<int:id>/', GoodsDetailView.as_view()),
    path('cart/', CartView.as_view()),
]
