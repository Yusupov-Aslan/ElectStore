from django.core.validators import BaseValidator
from django.db import models
from django.utils.deconstruct import deconstructible


# Create your models here.
CATEGORY_CHOICES = [("other", "Other"), ("laptops", "Laptops"), ("monitors", "Monitors"),
                    ("office_equipment", "Office equipment"), ("video_surveillance", "Video surveillance")]


class Product(models.Model):
    name_goods = models.CharField(max_length=100, verbose_name='Наименование товара')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Текст записи')
    # category = models.ForeignKey('ElectStore.Category', on_delete=models.PROTECT,
    #                              related_name='Category', verbose_name='Категории')
    category = models.CharField(max_length=20, default='other',
                                choices=CATEGORY_CHOICES, verbose_name='Категории')
    residue = models.PositiveIntegerField(verbose_name="Остаток")
    cost = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Стоимость')
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.pk}. {self.name_goods}: {self.category}"

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ItemCart(models.Model):
    product = models.ForeignKey('ElectStore.Product', on_delete=models.CASCADE,
                                related_name='item_carts', verbose_name='Категории')
    quantity = models.PositiveIntegerField(verbose_name="Количество")

    def __str__(self):
        return f"{self.pk}. {self.product}: {self.quantity}"

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'
