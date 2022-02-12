from django_registration.backends.activation.views import RegistrationView, ActivationView
from typing import Any, Dict

# Create your views here.


# class RegistrationView(RegistrationView):

#     def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         return context

#     def get_email_context(self, activation_key):
#         context = super().get_email_context(activation_key)
#         return context