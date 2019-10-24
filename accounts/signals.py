from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from accounts.models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
	Automatically create a profile when a new user 
	is created
    """
    if created:
        Profile.objects.create(user=instance)
        
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    Save new details when User object is updated
    """
    if instance:
        instance.profile.save()