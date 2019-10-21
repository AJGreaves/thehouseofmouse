from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Product(models.Model):
    """ model for product """
    WEIRD_MISC = 'WM'
    STAR_WARS = 'SW'
    OCCASIONS = 'OC'
    JOBS_HOBBIES = 'JH'
    HARRY_POTTER = 'HP'
    FAMOUS =  'FA'
    DOCTOR_WHO = 'DW'
    HALLOWEEN = 'HW'
    CHRISTMAS = 'CM'
    CATEGORY_CHOICES = [
        (WEIRD_MISC, 'Weird & Misc'),
        (STAR_WARS, 'Star Wars'),
        (OCCASIONS, 'Special Occasions'),
        (JOBS_HOBBIES, 'Jobs & Hobbies'),
        (HARRY_POTTER, 'Harry Potter'),
        (FAMOUS, 'Famous'),
        (DOCTOR_WHO, 'Doctor Who'),
        (HALLOWEEN, 'Halloween'),
        (CHRISTMAS, 'Christmas'),
    ]
    category = models.CharField(
        max_length=3,
        choices=CATEGORY_CHOICES,
        default=STAR_WARS,
    )
    title = models.CharField(max_length=100)
    # image1 = models.ImageField() have installed Pillow, but need to work out storage see https://docs.djangoproject.com/en/2.2/ref/models/fields/#imagefield
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    tags = models.CharField(max_length=300)
    num_in_stock = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100)])

    def __str__(self):
        return self.title
