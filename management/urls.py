from django.urls import path
from . import views

urlpatterns = {
    path('list/', views.ProductLIst, name="list"),
}
