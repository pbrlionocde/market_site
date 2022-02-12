

from frozendict import frozendict

from mainapp.forms import PhoneForm
from mainapp.models import Phone

CATEGORIES: frozendict = frozendict({
    'phone': (Phone, PhoneForm),
})
