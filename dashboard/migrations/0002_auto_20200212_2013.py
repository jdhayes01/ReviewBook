# Generated by Django 3.0.3 on 2020-02-13 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BookAdded',
        ),
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.CharField(default='Default', max_length=120, verbose_name='user'),
        ),
    ]
