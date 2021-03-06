# Generated by Django 4.0 on 2022-01-07 20:08

import cloudinary.models
from django.db import migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_car_number_of_doors_alter_car_production_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=cloudinary.models.CloudinaryField(default=django.utils.timezone.now, max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
    ]
