from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('brands/', views.brand, name='brand'),
    path('<str:slug>/', views.singlePost, name='single'),
    # create a product (CRUD operation)
    path('product/add/', views.addProduct, name='add'),
    path('collection/<slug:slug>/', views.collections, name='collection'),
    
]
