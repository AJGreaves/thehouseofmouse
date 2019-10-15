"""thehouseofmouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import home_view, faqs_view, about_view
from products.views import listing_view, results_view
# results_view can be used for search results, category or favourites

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    path('listing/', listing_view, name="listing"),
    path('results/', results_view, name="listing"),
    path('about/', about_view, name="about"),
    path('faqs/', faqs_view, name="faqs"),
]
