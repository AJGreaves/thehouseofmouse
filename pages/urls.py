from django.urls import path
from .views import faqs_view, about_view, contact_view

urlpatterns = [
    path('faqs/', faqs_view, name="faqs"),
    path('about/', about_view, name="about"),
    path('contact/', contact_view, name="contact")
]