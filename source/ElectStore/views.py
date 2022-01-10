from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from ElectStore.forms import ProductForm
from ElectStore.models import Product


def index_view(request):
    product = Product.objects.order_by("category", "name_goods")
    context = {'products': product}
    return render(request, 'index.html', context)


def one_product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'one_product.html', context)


def add_product_view(request, **kwargs):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'product_create.html', {"form": form})
    else:
        form = ProductForm(data=request.POST)

        if form.is_valid():
            category = form.cleaned_data.get('category')
            name_goods = form.cleaned_data.get('name_goods')
            description = form.cleaned_data.get('description')
            cost = form.cleaned_data.get('cost')
            residue = form.cleaned_data.get('residue')
            new_product = Product.objects.create(category=category, name_goods=name_goods, description=description,
                                                 cost=cost, residue=residue)
            new_product.save()
            return redirect("index")
        else:
            return render(request, 'product_create.html', {"form": form})