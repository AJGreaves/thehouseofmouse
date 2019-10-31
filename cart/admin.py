from django.contrib import admin
from .models import ShippingDestination, Order, OrderItem

# Register your models here.
admin.site.register(ShippingDestination)
admin.site.register(Order)
admin.site.register(OrderItem)