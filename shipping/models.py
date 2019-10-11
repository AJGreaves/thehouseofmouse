from django.db import models
# Create your models here.

class Destination_country(models.Model):
    name = models.CharField(max_length=100)
    shipping_category = models.ForeignKey(
        'Shipping_category',
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.name

class Shipping_category(models.Model):
    name = models.CharField(max_length=100)
    shipping_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name