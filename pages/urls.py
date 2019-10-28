from django.urls import path
from .views import faqs_view, about_view

urlpatterns = [
    path('faqs/', faqs_view, name="faqs"),
    path('about/', about_view, name="about"),
]