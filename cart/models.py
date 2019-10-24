from django.db import models
import datetime
from shipping.models import Destination_country
from products.models import Product

# Create your models here.

class Order(models.Model):

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    address_line_1 = models.CharField(max_length=150)
    address_line_2 = models.CharField(max_length=150, blank=True, null=True)
    town_or_city = models.CharField(max_length=150)
    county = models.CharField(max_length=150, blank=True, null=True)
    postcode = models.CharField(max_length=10)
    country = models.ForeignKey(
        Destination_country,
        on_delete=models.CASCADE,
        null=True,
    )
    date_ordered = models.DateField(default=datetime.date.today)
    shipped = models.BooleanField(default=False)

    def __str__(self):
        return f'Order placed on {self.date_ordered}'


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT
    )
    quantity = models.SmallIntegerField()
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Order item {self.product.title} quantity: {self.quantity}'