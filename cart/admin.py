from django.contrib import admin
from .models import ShippingDestination, Order, OrderItem

admin.site.register(ShippingDestination)
admin.site.register(Order)
admin.site.register(OrderItem)