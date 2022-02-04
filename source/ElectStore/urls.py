from django.urls import path

from ElectStore.views import one_product_view, add_product_view, update_product_view, delete_product_view, \
    IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/add/', add_product_view, name='add_product'),
    path('product/<int:pk>/', one_product_view, name='one_product'),
    path('product/<int:pk>/update/', update_product_view, name='update_product'),
    path('product/<int:pk>/delete/', delete_product_view, name='delete_product')

]
