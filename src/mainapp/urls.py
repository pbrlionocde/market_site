from django.urls import path

from mainapp.views import ProductsListView, ProductDeleteView, ProductCreateView

urlpatterns = [
    path('product/add/<category>', ProductCreateView.as_view(), name='add_product'),
    path('', ProductsListView.as_view(), name='list_goods'),
    path('<category>/<pk>/delete/', ProductDeleteView.as_view(), name='delete_product'),
]
