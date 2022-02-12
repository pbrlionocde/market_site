from typing import Any, Dict

from django.core import serializers
from django.db.models.query import QuerySet
from django.http import HttpResponseNotFound
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.views.generic.edit import DeleteView

from mainapp import views_config
from mainapp.models import Phone


# Create your views here.

class InvalidCategoryError(Exception):
    """Invalid category"""

class ProductCreateView(CreateView):
    # model = Phone
    # form_class = PhoneForm
    template_name = 'products/product.html'
    success_url = reverse_lazy('list_goods')

    def config_views(self):
        category = self.kwargs.get('category', '').lower()
        category_config = views_config.CATEGORIES.get(category)
        if category_config:
            model, form_class = category_config
            self.model = model
            self.form_class = form_class
        else:
            raise InvalidCategoryError()

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        try:
            self.config_views()
        except InvalidCategoryError:
            return HttpResponseNotFound('Incorrect category!!!')
        return super().get(request, *args, **kwargs)

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        try:
            self.config_views()
        except InvalidCategoryError:
            return HttpResponseNotFound('Incorrect category!!!')
        return super().post(request, *args, **kwargs)


class ProductDeleteView(DeleteView):
    # model = Phone
    template_name = 'products/confirm_delete.html'
    success_url = reverse_lazy('list_goods')

    def config_views(self):
        category = self.kwargs.get('category', '').lower()
        category_config = views_config.CATEGORIES.get(category)
        if category_config:
            model, _form_class = category_config
            self.model = model
        else:
            raise InvalidCategoryError()

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        try:
            self.config_views()
        except InvalidCategoryError:
            return HttpResponseNotFound('Incorrect category!!!')
        return super().get(request, *args, **kwargs)

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        try:
            self.config_views()
        except InvalidCategoryError:
            return HttpResponseNotFound('Incorrect category!!!')
        return super().post(request, *args, **kwargs)


class ProductsListView(ListView):

    model = Phone
    template_name = 'products/display_all.html'
    paginated_by = 100

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        for key, value in context.items():
            if isinstance(value, QuerySet):
                context[key] = serializers.serialize('json', value)
        return context
