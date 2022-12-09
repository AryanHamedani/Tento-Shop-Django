# Generated by Django 4.0.8 on 2022-12-09 10:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('promotions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='discountcode',
            name='available_to',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Useable by'),
        ),
    ]