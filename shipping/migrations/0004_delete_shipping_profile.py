# Generated by Django 2.2.6 on 2019-10-11 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_shipping_profile'),
        ('shipping', '0003_shipping_category_shipping_price'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Shipping_profile',
        ),
    ]
