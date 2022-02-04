from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
# Create your views here.
from ElectStore.forms import ProductForm
from ElectStore.models import Product


class IndexView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'index.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by("category", "name_goods")


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


def update_product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductForm(initial={
            'category': product.category,
            'name_goods': product.name_goods,
            'description': product.description,
            'cost': product.cost,
            'residue': product.residue,
        })
        return render(request, 'product_update.html', {"product": product, "form": form})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.category = form.cleaned_data.get('category')
            product.name_goods = form.cleaned_data.get('name_goods')
            product.description = form.cleaned_data.get('description')
            product.cost = form.cleaned_data.get('cost')
            product.residue = form.cleaned_data.get('residue')
            product.save()
            return redirect("index")
        else:
            return render(request, 'product_update.html', {"product": product, "form": form})


def delete_product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'products': product}
    if request.method == 'GET':
        return render(request, 'product_delete.html', context)
    else:
        product.delete()
        return redirect('index')