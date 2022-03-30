from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from api.views import ProductViewSet, OrderViewSet, ItemCartViewSet, ItemCartDeleteAPIView

app_name = 'api'

router = DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'order', OrderViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('cart/', ItemCartViewSet.as_view(), name='list_create_cart'),
    path('cart/<int:pk>/delete/', ItemCartDeleteAPIView.as_view(), name='delete_cart')
]
