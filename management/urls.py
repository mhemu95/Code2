from django.urls import path
from . import views


app_name = "management"
urlpatterns = [
    path('list/', views.ProductLIst, name="list"),
]
