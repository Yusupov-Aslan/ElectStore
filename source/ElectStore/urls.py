from django.urls import path

from ElectStore.views import (
    IndexView,
    ProductCreateView,
    ProductDetailView,
    ProductUpdateView,
    ProductDeleteView,
    CartAddView, CartView, CartDeleteView, OrderCreateView, OrderListView)

app_name = 'ElectStore'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/add/', ProductCreateView.as_view(), name='add_product'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='one_product'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='update_product'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete_product'),
    path('product/<int:pk>/cart/add/', CartAddView.as_view(), name='cart_add'),
    path('cart/', CartView.as_view(), name='cart_view'),
    path('cart/<int:pk>/delete/', CartDeleteView.as_view(), name='cart_delete'),
    path('order/create/', OrderCreateView.as_view(), name='order_create'),
    path('orders/', OrderListView.as_view(), name='orders')
]
