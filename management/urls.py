from django.urls import path
from . import views


app_name = "panel"
urlpatterns = [
    path('list/', views.ProductLIst, name="list"),
]
