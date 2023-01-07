# Generated by Django 4.0.8 on 2023-01-06 01:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0004_alter_maincategory_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', model_utils.fields.StatusField(choices=[(0, 'Pending for payment'), (1, 'Order paid and submitted'), (2, 'Customer received order successfully')], default=0, max_length=100, no_check_for_status=True, verbose_name='Order Status')),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', verbose_name='Order status change date')),
                ('description', models.TextField(blank=True, verbose_name='Order Description')),
                ('total_price', models.DecimalField(decimal_places=0, default=0, max_digits=10, verbose_name='Total Price')),
                ('final_price', models.DecimalField(decimal_places=0, default=0, max_digits=10, verbose_name='Final Price')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='Order Owner')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=0, default=0, max_digits=10, verbose_name='Price')),
                ('quantity', models.PositiveIntegerField(verbose_name='Ordered Quantity')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='shop.productvariety', verbose_name='Product Item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order', verbose_name='Order')),
            ],
        ),
    ]