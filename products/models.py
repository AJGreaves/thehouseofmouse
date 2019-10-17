from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Product(models.Model):
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        null=True
    )
    title = models.CharField(max_length=100)
    # image1 = models.ImageField() have installed Pillow, but need to work out storage see https://docs.djangoproject.com/en/2.2/ref/models/fields/#imagefield
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    tags = models.CharField(max_length=300)
    num_in_stock = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100)])
    title_tag = models.CharField(max_length=60, default='')

    def __str__(self):
        return self.title
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name