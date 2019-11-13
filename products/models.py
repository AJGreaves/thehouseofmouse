from django.db import models
from django.core.validators import MaxValueValidator
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    """ Model for product """
    WEIRD_MISC = 'Weird & Misc'
    STAR_WARS = 'Star Wars'
    OCCASIONS = 'Special Occasions'
    JOBS_HOBBIES = 'Jobs & Hobbies'
    HARRY_POTTER = 'Harry Potter'
    FAMOUS = 'Famous'
    DOCTOR_WHO = 'Doctor Who'
    HALLOWEEN = 'Halloween'
    CHRISTMAS = 'Christmas'
    CATEGORY_CHOICES = [
        (WEIRD_MISC, 'Weird & Misc'),
        (STAR_WARS, 'Star Wars'),
        (OCCASIONS, 'Special Occasions'),
        (JOBS_HOBBIES, 'Jobs & Hobbies'),
        (HARRY_POTTER, 'Harry Potter'),
        (FAMOUS, 'Famous'),
        (DOCTOR_WHO, 'Doctor Who'),
        (HALLOWEEN, 'Halloween'),
        (CHRISTMAS, 'Christmas'),
    ]
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default=STAR_WARS,
    )
    title = models.CharField(max_length=100)
    product_image1 = models.ImageField(upload_to="product_images", blank=True)
    product_image2 = models.ImageField(upload_to="product_images", blank=True, null=True)
    product_image3 = models.ImageField(upload_to="product_images", blank=True, null=True)
    product_image4 = models.ImageField(upload_to="product_images", blank=True, null=True)
    product_image5 = models.ImageField(upload_to="product_images", blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    tags = models.CharField(max_length=300)
    num_in_stock = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100)])
    featured = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('listing-detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.title
