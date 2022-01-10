from django.shortcuts import render, get_object_or_404

# Create your views here.
from ElectStore.models import Product


def index_view(request):
    product = Product.objects.order_by("category", "name_goods")
    context = {'products': product}
    return render(request, 'index.html', context)


def one_product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'one_product.html', context)