from django.contrib import admin
from django.urls import path
from mainapp.views import PhoneCreateView, GoodsListView

urlpatterns = [
    path('goods/add/phone', PhoneCreateView.as_view(), name='phone_add'),
    path('goods/list_all/', GoodsListView.as_view(), name='list_goods'),
]
