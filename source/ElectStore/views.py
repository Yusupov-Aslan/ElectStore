import json
from urllib.parse import urlencode
from urllib.request import Request

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.sessions.models import Session
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
# Create your views here.
from ElectStore.forms import ProductForm, SearchForm, OrderForm
from ElectStore.models import Product, ItemCart, Order, OrderProduct


class IndexView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'index.html'
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(name_goods__icontains=self.search_value)
            queryset = queryset.filter(query)
        queryset = queryset.filter(residue__gt=0)
        return queryset.order_by("category", "name_goods")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = SearchForm()
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search'] = self.search_value
        return context

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search')
        return None


class ProductCreateView(PermissionRequiredMixin, CreateView):
    permission_required = "ElectStore:add_product"
    model = Product
    form_class = ProductForm
    template_name = "products/product_create.html"

    def get_success_url(self):
        return reverse("ElectStore:one_product", kwargs={"pk": self.object.pk})


class ProductDetailView(DetailView):
    template_name = 'products/one_product.html'
    model = Product


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = "ElectStore:change_product"
    model = Product
    template_name = 'products/product_update.html'
    form_class = ProductForm

    def get_success_url(self):
        return reverse("ElectStore:one_product", kwargs={"pk": self.object.pk})


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = "ElectStore:delete_product"
    model = Product
    template_name = 'products/product_delete.html'
    success_url = reverse_lazy('ElectStore:index')


class CartView(ListView):
    model = ItemCart
    template_name = "item_cart.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        arr = []
        # for item in context['object_list']:
        #     arr.append(item.product.cost * item.quantity)
        cart = json.loads(self.request.COOKIES.get("cart")) if "cart" in self.request.COOKIES else []
        for item in cart:
            arr.append(item["product_cost"] * item["amount"])
        context['total'] = sum(arr)
        context['form'] = OrderForm()
        return context


class CartAddView(View):
    def post(self, request: Request, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.get(pk=pk)
        if product.residue > 0:
            url = reverse("ElectStore:index")
            res = HttpResponseRedirect(url)
            if request.POST.get("site"):
                res = HttpResponseRedirect(request.POST.get("site"))
            if request.POST.get('page'):
                res = HttpResponseRedirect(f'{url}?page={request.POST.get("page")}')
            cart = json.loads(request.COOKIES.get("cart")) if "cart" in request.COOKIES else []
            try:
                cart_item = next(item for item in cart if item["product_id"] == product.id)
                if product.residue >= cart_item['amount']+1:
                    cart_item['amount'] += 1
            except:
                cart_item = {
                    "product_id": product.id,
                    "amount": 1,
                    "product_name": product.name_goods,
                    "product_cost": float(product.cost)}
                cart.append(cart_item)
            res.set_cookie(key="cart", value=json.dumps(cart))


        return res


class CartDeleteView(DeleteView):
    model = ItemCart
    template_name = 'item_cart.html'

    def post(self, request, *args, **kwargs):
        # self.object = self.get_object()
        # product = self.object.product
        # product.residue += self.object.quantity
        # product.save()
        pk = self.kwargs.get(self.pk_url_kwarg)
        cart = json.loads(request.COOKIES.get("cart"))
        cart_item = next(item for item in cart if item["product_id"] == pk)
        cart_item['amount'] -= 1
        if cart_item['amount'] <= 0:
            cart.remove(cart_item)
        res = HttpResponseRedirect(self.get_success_url())
        res.set_cookie(key="cart", value=json.dumps(cart))
        return res

    def get_success_url(self):
        return reverse("ElectStore:cart_view")


class OrderCreateView(View):
    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in ItemCart.objects.all():
                OrderProduct.objects.create(order=order, product=item.product, amount=item.quantity)
            ItemCart.objects.all().delete()
        return redirect('ElectStore:cart_view')
