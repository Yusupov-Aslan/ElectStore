from django.urls import path

from ElectStore.views import index_view, one_product_view, add_product_view, update_product_view, delete_product_view

urlpatterns = [
    path('', index_view, name='index'),
    path('product/<int:pk>/', one_product_view, name='one_product'),
    path('product/add/', add_product_view, name='add_product'),
    path('product/update/<int:pk>/', update_product_view, name='update_product'),
    path('delete/<int:pk>/', delete_product_view, name='delete_product')

]
