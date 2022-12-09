# Generated by Django 4.0.8 on 2022-12-09 10:32

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Province name')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='City name')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addresses.province', verbose_name='Province name')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.TextField(verbose_name='Street Address')),
                ('number', models.PositiveSmallIntegerField(verbose_name='Building Number')),
                ('unit', models.PositiveSmallIntegerField(verbose_name='Unit Number')),
                ('postal_code', models.CharField(max_length=10, verbose_name='Postal Code')),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='Address Location')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Address Title')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addresses.city', verbose_name='City')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
