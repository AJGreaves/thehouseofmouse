from django.db import models
# Create your models here.
class Shipping_profile(models.Model):
    name = models.CharField(max_length=100)
    price_nl = models.DecimalField(max_digits=6, decimal_places=2)
    price_eu = models.DecimalField(max_digits=6, decimal_places=2)
    price_non_eu = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return self.name