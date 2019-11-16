from django.views.generic import ListView
from .models import GalleryItem

class GalleryView(ListView):
    model = GalleryItem
    template_name = 'gallery.html'
    context_object_name = 'gallery_items'
    paginate_by = 24
