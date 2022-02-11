from django.urls import path

from mainapp.views import GoodsListView, PhoneCreateView, PhoneDeleteView

urlpatterns = [
    path('goods/add/phone', PhoneCreateView.as_view(), name='phone_add'),
    path('goods/list_all/', GoodsListView.as_view(), name='list_goods'),
    path('<pk>/delete_phone/', PhoneDeleteView.as_view(), name='delete_phone'),
]
