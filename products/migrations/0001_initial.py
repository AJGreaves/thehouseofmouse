# Generated by Django 2.2.6 on 2019-10-31 11:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Weird & Misc', 'Weird & Misc'), ('Star Wars', 'Star Wars'), ('Special Occasions', 'Special Occasions'), ('Jobs & Hobbies', 'Jobs & Hobbies'), ('Harry Potter', 'Harry Potter'), ('Famous', 'Famous'), ('Doctor Who', 'Doctor Who'), ('Halloween', 'Halloween'), ('Christmas', 'Christmas')], default='Star Wars', max_length=20)),
                ('title', models.CharField(max_length=100)),
                ('product_image1', models.ImageField(upload_to='product_images')),
                ('product_image2', models.ImageField(blank=True, null=True, upload_to='product_images')),
                ('product_image3', models.ImageField(blank=True, null=True, upload_to='product_images')),
                ('product_image4', models.ImageField(blank=True, null=True, upload_to='product_images')),
                ('product_image5', models.ImageField(blank=True, null=True, upload_to='product_images')),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('tags', models.CharField(max_length=300)),
                ('num_in_stock', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(100)])),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
    ]
