# from django.shortcuts import render
from django.views.generic import CreateView, ListView
from mainapp.models import Phone
from django.urls import reverse_lazy

from typing import Any, Dict

# Create your views here.


class PhoneCreateView(CreateView):
    model = Phone
    template_name = 'goods/phone.html'
    success_url = reverse_lazy('phone_add')
    fields = ['manufacturer', 'model', 'display', 'processor', 'number_cores']


class GoodsListView(ListView):

    model = Phone
    template_name = 'goods/display_all.html'
    paginated_by = 100

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context