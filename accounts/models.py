from django.db import models
from django.contrib.auth.models import User
from shipping.models import Destination_country

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=150, null=True)
    address_line_2 = models.CharField(max_length=150, blank=True, null=True)
    town_or_city = models.CharField(max_length=150, null=True)
    county = models.CharField(max_length=150, blank=True, null=True)
    postcode = models.CharField(max_length=10, null=True)
    country = models.ForeignKey(
        Destination_country,
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return f'{self.user.username} Profile'
