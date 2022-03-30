from rest_framework import serializers
from ElectStore.models import Product, Order, ItemCart


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class ItemCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCart
        fields = "__all__"
        read_only_fields = ('user',)
