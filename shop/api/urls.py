from django.urls import path

from .views import super_category


urlpatterns = [
    path('super-category/', super_category)
]
