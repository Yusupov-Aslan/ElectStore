from django import forms

from ElectStore.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("category", "name_goods", "description", "cost", "residue")


class SearchForm(forms.Form):
    search = forms.CharField(max_length=40, required=False, label="Найти")
