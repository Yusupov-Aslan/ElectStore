from django.contrib import admin

from ElectStore.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'name_goods']
    list_filter = ['category']
    search_fields = ['category']
    fields = ['category', 'name_goods', 'description', 'cost', 'residue']
    readonly_fields = ['created_at']


admin.site.register(Product, ProductAdmin)
