# Generated by Django 4.0.8 on 2022-12-09 10:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('description', models.TextField(verbose_name='Order Description')),
                ('order_date', models.DateTimeField(auto_now_add=True, verbose_name='Order Date')),
                ('total_price', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Total Price')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=0, max_digits=10, verbose_name='Price')),
                ('quantity', models.PositiveIntegerField(verbose_name='Ordered Quantity')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productitem', verbose_name='Product Item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='Order')),
            ],
        ),
    ]
