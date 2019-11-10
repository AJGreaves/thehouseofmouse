from django.urls import path
from .views import faqs_view, about_view, contact_view, privacy_view, terms_view

urlpatterns = [
    path('faqs/', faqs_view, name="faqs"),
    path('about/', about_view, name="about"),
    path('contact/', contact_view, name="contact"),
    path('privacy/', privacy_view, name="privacy"),
    path('terms-and-conditions/', terms_view, name="terms")
]
