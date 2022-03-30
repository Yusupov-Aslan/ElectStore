from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from ElectStore.models import Product, Order, ItemCart
from api.exceptions import InvalidDataException
from api.permissions import IsStaffPermission, OrderPermission, IsCartItemOwner
from api.serializers import ProductSerializer, OrderSerializer, ItemCartSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsStaffPermission,)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (OrderPermission,)


class ItemCartViewSet(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user = request.user
        cart = user.cart_items.all()
        serializer = ItemCartSerializer(cart, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        user = request.user
        serializer = ItemCartSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = serializer.validated_data.get('product')
        quantity = serializer.validated_data.get('quantity')
        if product.residue < quantity:
            raise InvalidDataException
        serializer.save(user=user)
        product.residue -= quantity
        product.save()
        return Response(serializer.data)


class ItemCartDeleteAPIView(APIView):
    permission_classes = (IsAuthenticated, IsCartItemOwner,)

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        product = obj.product
        product.residue += obj.quantity
        product.save()
        obj.delete()
        return Response(status=200, data={'success': True})

    def get_object(self):
        queryset = self.request.user.cart_items.all()
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(queryset, id=pk)
        self.check_object_permissions(self.request, obj)
        return obj
