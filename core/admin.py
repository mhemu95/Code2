from django.contrib import admin
from .models import Brand, Product


class ProductAdmin(admin.ModelAdmin):

    list_display = ('prod_name', 'prod_tag', 'prod_price', 'offer_price')
    prepopulated_fields = {'prod_slug': ('prod_name', )}


admin.site.register(Product, ProductAdmin)


class BrandAdmin(admin.ModelAdmin):

    list_display = ('brand_name',)
    prepopulated_fields = {'brand_slug': ('brand_name', )}


admin.site.register(Brand, BrandAdmin)
