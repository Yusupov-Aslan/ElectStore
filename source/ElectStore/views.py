from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
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


class ProductDetailView(DetailView):
    template_name = 'one_product.html'
    model = Product


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_update.html'
    form_class = ProductForm

    def get_success_url(self):
        return reverse("one_product", kwargs={"pk": self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('index')
