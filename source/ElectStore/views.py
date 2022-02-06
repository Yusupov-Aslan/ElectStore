from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView
# Create your views here.
from ElectStore.forms import ProductForm
from ElectStore.models import Product


class IndexView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'index.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(residue__gt=0)
        return queryset.order_by("category", "name_goods")


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product_create.html"

    def get_success_url(self):
        return reverse("one_product", kwargs={"pk": self.object.pk})


def one_product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'one_product.html', context)


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