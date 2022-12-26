# Generated by Django 4.0.8 on 2022-12-23 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_remove_productvariety_price_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maincategory',
            name='slug',
        ),
        migrations.AlterField(
            model_name='productimagegallery',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop.product', verbose_name='Product'),
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='parent',
        ),
        migrations.AddField(
            model_name='subcategory',
            name='parent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='shop.maincategory', verbose_name='Parent'),
            preserve_default=False,
        ),
    ]