from django.db import models
import datetime
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.

class Order(models.Model):

    customer = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    full_name = models.CharField(max_length=150, null=True)
    address_line_1 = models.CharField(max_length=150, null=True)
    address_line_2 = models.CharField(max_length=150, blank=True, null=True)
    town_or_city = models.CharField(max_length=150, null=True)
    county = models.CharField(max_length=150, blank=True, null=True)
    postcode = models.CharField(max_length=10, null=True)
    # country = models.ForeignKey(Destination_country, on_delete=models.CASCADE, null=True)
    date_ordered = models.DateField(default=datetime.date.today, null=True)
    paid = models.BooleanField(default=False)
    shipped = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}-{self.date_ordered}-{self.full_name}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.quantity} x {self.product.title}'
