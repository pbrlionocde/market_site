from django import forms

from mainapp.constant import CLASS, FORM_FIELD
from mainapp.models import Phone


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = [
            'manufacturer',
            'category',
            'code_of_product',
            'price',
            'weight',
            'producing_country',
            'model',
            'display',
            'processor',
            'number_cores',
            'image_url',
        ]
        widgets = {
            'manufacturer': forms.TextInput(attrs={CLASS: FORM_FIELD}),
            'category': forms.TextInput(attrs={CLASS: FORM_FIELD}),
            'code_of_product': forms.NumberInput(attrs={CLASS: FORM_FIELD}),
            'price': forms.NumberInput(attrs={CLASS: FORM_FIELD}),
            'weight': forms.NumberInput(attrs={CLASS: FORM_FIELD}),
            'producing_country': forms.TextInput(attrs={CLASS: FORM_FIELD}),
            'model': forms.TextInput(attrs={CLASS: FORM_FIELD}),
            'display': forms.NumberInput(attrs={CLASS: FORM_FIELD}),
            'processor': forms.TextInput(attrs={CLASS: FORM_FIELD}),
            'number_cores': forms.NumberInput(attrs={CLASS: FORM_FIELD}),
            'image_url': forms.URLInput(attrs={CLASS: FORM_FIELD}),
        }
