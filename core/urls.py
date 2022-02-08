from django.urls import path
from . import views

app_name = "core"
urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('brands/', views.brand, name='brand'),
    path('categories/', views.category, name='category'),
    path('<str:slug>/', views.singlePost, name='single'),

    # create a product (CRUD operation)
    path('product/add/', views.addProduct, name='product-add'),
    path('category/add/', views.addCategory, name='category-add'),
    path('brand/add/', views.addBrand, name='brand-add'),

    # update
    path('product/update/<slug:slug>/',
         views.updateProduct, name='update-product'),
    path('category/update/<slug:slug>/',
         views.updateCategory, name='update-category'),
    path('brand/update/<slug:slug>/',
         views.updateBrand, name='update-brand'),

    # delete a product
    path('product/delete/<slug:slug>/', views.deleteProduct, name='delete-product'),
    path('category/delete/<slug:slug>/', views.deleteCategory, name='delete-category'),
    path('category/brand/<slug:slug>/', views.deleteBrand, name='delete-brand'),

    # products by brand
    path('collection/<slug:slug>/', views.collections, name='collection'),
    path('category/collection/<slug:slug>/',
         views.prodByCat, name='collection2'),

]
