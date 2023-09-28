from django import forms
from . models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'types': forms.TextInput(attrs={'class': 'form-control'}),
            'cat_of_products': forms.TextInput(attrs={'class': 'form-control'}),
        }
