# Generated by Django 4.0.8 on 2022-12-09 01:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Promotion Name')),
                ('rate', models.PositiveSmallIntegerField(verbose_name='Discount Percentage')),
                ('max_amount', models.PositiveIntegerField(verbose_name='Discount Max Amount')),
                ('description', models.TextField(blank=True, verbose_name='Promotion Description')),
                ('start_date', models.DateTimeField(verbose_name='Promotion Start Date and Time')),
                ('end_date', models.DateTimeField(verbose_name='Promotion End Date and Time')),
                ('item', models.ManyToManyField(to='products.productitem', verbose_name='Item To Promote')),
            ],
        ),
        migrations.CreateModel(
            name='DiscountCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.UUIDField(verbose_name='Discount Code')),
                ('rate', models.PositiveSmallIntegerField(verbose_name='Discount Percentage')),
                ('max_amount', models.PositiveIntegerField(verbose_name='Discount Max Amount')),
                ('available_to', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Useable by')),
            ],
        ),
    ]
