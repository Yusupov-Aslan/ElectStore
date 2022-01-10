from django import forms
from django.forms import widgets

from ElectStore.models import CATEGORY_CHOICES


class ProductForm(forms.Form):
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=True, label='Категории',
                                 initial=CATEGORY_CHOICES[0][1])
    name_goods = forms.CharField(max_length=100, required=True, label='Наименование')
    description = forms.CharField(max_length=2000, required=False, label='Описание',
                                  widget=widgets.Textarea(attrs={"rows": 2, "cols": 30}))
    cost = forms.DecimalField(max_digits=9, decimal_places=2, label='Стоимость')
    residue = forms.IntegerField(min_value=0, label="Остаток")



