from django.urls import path
from . import views

app_name = "core"
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('brands/', views.brand, name='brand'),
    path('categories/', views.category, name='category'),
    path('<str:slug>/', views.singlePost, name='single'),

    # create a product (CRUD operation)
    #path('product/add/', views.addProduct, name='add'),

    # products by brand
    path('collection/<slug:slug>/', views.collections, name='collection'),
    path('category/collection/<slug:slug>/',
         views.prodByCat, name='collection2'),

]
