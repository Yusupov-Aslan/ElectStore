from rest_framework import serializers
from ElectStore.models import Product, Order, ItemCart, OrderProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ("product", "amount",)
        depth = 1


class OrderSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = "__all__"

    def get_products(self, obj):
        queryset = OrderProduct.objects.filter(order=obj)
        return OrderProductSerializer(queryset, many=True).data


class ItemCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCart
        fields = "__all__"
        read_only_fields = ('user',)
