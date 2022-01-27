from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'prod_name',
            'prod_slug',
            'prod_price',
            'offer_price',
            'prod_img',
            'prod_tag',
            'prod_details',
        ]