from django.urls import path

from ElectStore.views import (
    IndexView,
    ProductCreateView,
    ProductDetailView,
    ProductUpdateView,
    ProductDeleteView)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/add/', ProductCreateView.as_view(), name='add_product'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='one_product'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='update_product'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete_product')

]
