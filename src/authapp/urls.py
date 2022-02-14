from django.urls import include, path
from django.contrib import admin
from authapp.views import UserView, AddGroup

urlpatterns = [
    path('admin/', admin.site.urls),
    # path(
    #     'accounts/register/',
    #     RegistrationView.as_view(success_url='/'),
    #     name='django_registration_register',
    # ),
    path('users/', UserView.as_view()),
    path('user/<pk>/add_to_group', AddGroup.as_view()),
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

