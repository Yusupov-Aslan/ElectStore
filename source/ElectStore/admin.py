from django.contrib.auth.models import Permission
from django.contrib.sessions.models import Session

from ElectStore.models import Product, Order
from django.contrib import admin


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'name_goods']
    list_filter = ['category']
    search_fields = ['category']
    fields = ['category', 'name_goods', 'description', 'cost', 'residue']
    readonly_fields = ['created_at']


class ProductInline(admin.TabularInline):
    model = Order.products.through
    readonly_fields = ('product', 'amount')
    can_delete = False
    extra = 0

    def has_add_permission(self, request, obj):
        return False


class OrederAdmin(admin.ModelAdmin):
    fields = ['user', 'phone', 'address']
    list_display = ('pk', 'phone', 'address', 'created_at')
    readonly_fields = ['created_at']
    inlines = (ProductInline,)
    ordering = ('-created_at',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrederAdmin)
admin.site.register(Permission)
admin.site.register(Session)
