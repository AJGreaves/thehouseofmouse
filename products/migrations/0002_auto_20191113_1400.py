# Generated by Django 2.2.6 on 2019-11-13 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image1',
            field=models.ImageField(blank=True, upload_to='product_images'),
        ),
    ]
