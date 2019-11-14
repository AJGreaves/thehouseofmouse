from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from pages.views import home_view

urlpatterns = [

    path('', home_view, name="home"),
    path('pages/', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('search/', include('search.urls')),

    path('admin/', admin.site.urls),
]

# only add this in when in debug mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
