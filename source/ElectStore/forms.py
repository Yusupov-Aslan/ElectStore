from django import forms
from django.forms import widgets

from ElectStore.models import CATEGORY_CHOICES, Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("category", "name_goods", "description", "cost", "residue")




