# Generated by Django 3.0.3 on 2020-02-13 10:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20200212_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='book',
            name='review_desc',
            field=models.TextField(default='Enter Description Here'),
        ),
    ]