from django.db import models

class GalleryItem(models.Model):
    """ Model for gallery images and descriptions """
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="product_images")
    description = models.TextField()

    def __str__(self):
        return self.name