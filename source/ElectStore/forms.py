from django import forms

from ElectStore.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("category", "name_goods", "description", "cost", "residue")




