from django import forms

from .constant import MAX_LEN_NAME


class PhoneForm(forms.Form):
    """Form for phone items"""

    manufacturer = forms.CharField(max_length=MAX_LEN_NAME, required=True)
    model = forms.CharField(max_length=MAX_LEN_NAME, required=True)
    display = forms.IntegerField(label='Display', required=True)
    processor = forms.CharField(max_length=40, label='Processor', required=True)
    number_cores = forms.IntegerField(label='Number cores', required=True)
