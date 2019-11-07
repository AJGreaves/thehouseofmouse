from django.urls import path
from .views import search_view

urlpatterns = [
    path('', search_view, name='search'),
    path('/<str:search_input>', search_view, name='search-results'),
]
