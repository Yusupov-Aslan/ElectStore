from rest_framework import viewsets
from ElectStore.models import Product, Order
from api.permissions import IsStaffPermission, OrderPermission
from api.serializers import ProductSerializer, OrderSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsStaffPermission,)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (OrderPermission,)



