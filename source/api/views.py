from rest_framework import viewsets
from ElectStore.models import Product
from api.permissions import IsStaffPermission
from api.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsStaffPermission,)



