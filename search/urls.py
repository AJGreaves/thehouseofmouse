from django.urls import path
from .views import search_view, search_results_view

urlpatterns = [
    path('', search_view, name='search'),
    path('<slug:query>', search_results_view, name='search-results')
]
