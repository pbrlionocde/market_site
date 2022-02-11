from typing import Any, Dict

from django.core import serializers
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.views.generic.edit import DeleteView

from mainapp.forms import PhoneForm
from mainapp.models import Phone

# Create your views here.


class PhoneCreateView(CreateView):
    model = Phone
    form_class = PhoneForm
    template_name = 'goods/phone.html'
    success_url = reverse_lazy('phone_add')


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
        for key, value in context.items():
            if isinstance(value, QuerySet):
                context[key] = serializers.serialize('json', value)
        return context
