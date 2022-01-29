from django.contrib import admin
from .models import Brand, Product, Category


class ProductAdmin(admin.ModelAdmin):

    list_display = ('prod_name', 'prod_tag', 'prod_price', 'offer_price')
    prepopulated_fields = {'prod_slug': ('prod_name', )}


admin.site.register(Product, ProductAdmin)


class BrandAdmin(admin.ModelAdmin):

    list_display = ('brand_name',)
    prepopulated_fields = {'brand_slug': ('brand_name', )}


admin.site.register(Brand, BrandAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_status',)
    prepopulated_fields = {'category_slug': ('category_name',)}


admin.site.register(Category, CategoryAdmin)
