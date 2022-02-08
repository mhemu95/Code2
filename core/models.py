from django.db import models
from django.urls import reverse


class Brand(models.Model):
    brand_name = models.CharField(max_length=150, null=False, blank=False)
    brand_slug = models.SlugField(max_length=150, null=False, unique=True)
    brand_image = models.ImageField(upload_to='Brands', blank=False)
    brand_status = models.BooleanField(default=True, null=False)

    class Meta:
        ordering = ['brand_name']

    def __str__(self):
        return self.brand_name


class Product(models.Model):
    brands = models.ForeignKey('Brand', on_delete=models.CASCADE)
    category = models.ForeignKey(
        "Category", default=1, on_delete=models.SET_DEFAULT)
    prod_name = models.CharField(max_length=150, null=False, blank=False)
    prod_slug = models.SlugField(max_length=150, null=False, unique=True)
    prod_price = models.FloatField(null=False)
    offer_price = models.FloatField(blank=True, null=True)
    prod_img = models.ImageField(upload_to='products', blank=False, null=True)
    prod_tag = models.CharField(max_length=20, unique=True, null=False)
    prod_details = models.TextField(default='coming soon')
    Prod_created = models.DateTimeField(auto_now_add=True)
    prod_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-Prod_created']

    def get_absolute_url(self):
        return reverse('single', kwargs={'slug': self.prod_slug})

    def __str__(self):
        return self.prod_name


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    category_slug = models.CharField(max_length=50)
    category_status = models.BooleanField(default=True, null=False)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name
