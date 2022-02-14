from typing import Any

from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.models import User
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, detail

from authapp.forms import NewAdmin
from authapp.group import get_group_admin


class GroupRequiredMixin(AccessMixin):

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        for group in request.user.groups.values_list('name', flat=True):
            if group in self.allowed_groups:
                return super().dispatch(request, *args, **kwargs)
        return self.handle_no_permission()


class UserView(GroupRequiredMixin, ListView):
    model = User
    template_name = 'users.html'
    allowed_groups = ('Admin',)


class AddGroup(GroupRequiredMixin, detail.SingleObjectMixin, FormView):
    model = User
    form_class = NewAdmin
    query_pk_and_slug = True
    context_object_name = 'user'
    template_name = 'user_add_to_group.html'
    success_url = reverse_lazy('list_goods')

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.object = self.get_object()     # pylint: disable=attribute-defined-outside-init
        return super().get(request, *args, **kwargs)

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        self.object = self.get_object()     # pylint: disable=attribute-defined-outside-init
        return super().post(request, *args, **kwargs)

    def form_valid(self, form) -> HttpResponse:
        if form.cleaned_data.pop('admin', None):
            group = get_group_admin()
            self.object.groups.add(group)
        return super().form_valid(form)
