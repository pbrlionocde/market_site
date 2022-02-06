# from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.views.generic.edit import DeleteView
from mainapp.models import Phone
from django.urls import reverse_lazy
from .forms import PhoneForm

from typing import Any, Dict

# Create your views here.


class PhoneCreateView(CreateView):
    model = Phone
    form_class = PhoneForm
    template_name = 'goods/phone.html'

    success_url = reverse_lazy('phone_add')
    # fields = ['manufacturer', 'category', 'weight', 'producing_country', 'model', 'display', 'processor', 'number_cores', 'image_url']


class PhoneDeleteView(DeleteView):
    model = Phone
    template_name = 'goods/phone_confirm_delete.html'
    success_url = reverse_lazy('list_goods')

class GoodsListView(ListView):

    model = Phone
    template_name = 'goods/display_all.html'
    paginated_by = 100

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context