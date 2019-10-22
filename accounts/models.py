from django.db import models
from django.contrib.auth.models import User
from shipping.models import Destination_country

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=150)
    address2 = models.CharField(max_length=150, blank=True, null=True)
    town = models.CharField(max_length=150)
    county = models.CharField(max_length=150, blank=True, null=True)
    postcode = models.CharField(max_length=10)
    country = models.ForeignKey(
        Destination_country,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.user.username} Profile'