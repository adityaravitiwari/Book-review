# Generated by Django 4.1.7 on 2023-06-25 07:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
