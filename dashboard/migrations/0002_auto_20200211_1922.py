# Generated by Django 3.0.3 on 2020-02-12 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookadded',
            name='book_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.Book'),
        ),
    ]
