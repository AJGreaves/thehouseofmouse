from django.db import models
import datetime
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.
class ShippingDestination(models.Model):
    """ Model to store all shipping destinations with their relevant price and shipping time """

    country = models.CharField(max_length=50)
    shipping_price = models.DecimalField(max_digits=6, decimal_places=2)
    shipping_time = models.CharField(max_length=150, default="1 to 2 weeks")

    def __str__(self):
        return f'{self.country}'

class Order(models.Model):
    """
    Model to store order information, customer, shipping address,
    date ordered and if the order has been paid or shipped yet.
    """

    customer = models.ForeignKey(User, on_delete=models.PROTECT)
    full_name = models.CharField(max_length=150, null=True)
    address_line_1 = models.CharField(max_length=150, null=True)
    address_line_2 = models.CharField(max_length=150, blank=True, null=True)
    town_or_city = models.CharField(max_length=150, null=True)
    county = models.CharField(max_length=150, blank=True, null=True)
    postcode = models.CharField(max_length=10, null=True)
    country = models.ForeignKey(ShippingDestination, on_delete=models.PROTECT, null=True)
    date_ordered = models.DateField(default=datetime.date.today, null=True)
    paid = models.BooleanField(default=False)
    shipped = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}-{self.date_ordered}-{self.customer.username}'

class OrderItem(models.Model):
    """
    Model to store individual order items, the Order and Product they relate
    to and the quantity the customer would like.
    """
    
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.quantity} x {self.product.title}'
