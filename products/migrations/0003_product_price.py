# Generated by Django 4.2.5 on 2023-09-29 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_price_product_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
