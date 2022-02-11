from django import forms
from .models import Phone
from .constant import MAX_LEN_NAME


class PhoneForm(forms.ModelForm):
    """Form for phone items"""
    class Meta:
        model = Phone
        fields = ['manufacturer', 'category', 'code_of_product', 'price', 'weight', 'producing_country', 'model', 'display', 'processor', 'number_cores', 'image_url']
        widgets = {
            'manufacturer': forms.TextInput(attrs={'class': 'FormField'}),
            'category': forms.TextInput(attrs={'class': 'FormField'}),
            'code_of_product': forms.NumberInput(attrs={'class': 'FormField'}),
            'price': forms.NumberInput(attrs={'class': 'FormField'}),
            'weight': forms.NumberInput(attrs={'class': 'FormField'}),
            'producing_country': forms.TextInput(attrs={'class': 'FormField'}), 
            'model': forms.TextInput(attrs={'class': 'FormField'}), 
            'display': forms.NumberInput(attrs={'class': 'FormField'}), 
            'processor': forms.TextInput(attrs={'class': 'FormField'}), 
            'number_cores': forms.NumberInput(attrs={'class': 'FormField'}),
            'image_url': forms.URLInput(attrs={'class': 'FormField'})
        }


# class ItemFrom(forms.Form):
#     """Form for base item"""

#     category = forms.CharField(max_length=MAX_LEN_NAME, required=True)
#     weight = forms.FloatField()
