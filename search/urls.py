from django.urls import path
from .views import search_view

urlpatterns = [
    path('/results/<str:search_input>', search_view, name='search'),
]
