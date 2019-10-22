from django.db import models
from django.contrib.auth.models import User
from shipping.models import Destination_country
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=150, null=True)
    address2 = models.CharField(max_length=150, blank=True, null=True)
    town = models.CharField(max_length=150, null=True)
    county = models.CharField(max_length=150, blank=True, null=True)
    postcode = models.CharField(max_length=10, null=True)
    country = models.ForeignKey(
        Destination_country,
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return f'{self.user.username} Profile'


"""
These signals should be in their own signals.py file. 
But for some reason I cannot get them to work from there.
"""
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    """
	Automatically create a profile when a new user 
	is created
    """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_profile(sender, instance, **kwargs):
    """
    Save new details when User object is updated
    """
    if instance:
        instance.profile.save()