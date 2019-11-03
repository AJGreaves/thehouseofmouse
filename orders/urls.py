from django.urls import path
from .views import orders_view

urlpatterns = [
    path('', orders_view, name="orders"),
]