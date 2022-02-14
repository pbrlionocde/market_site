
from django import forms


class NewAdmin(forms.Form):
    admin = forms.BooleanField(widget=forms.CheckboxInput)

    class Meta:
        fields = ('admin',)
