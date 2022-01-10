from django.urls import path

from ElectStore.views import index_view, one_product_view

urlpatterns = [
    path('', index_view, name='index'),
    path('product/<int:pk>/', one_product_view, name='one_product')
]
