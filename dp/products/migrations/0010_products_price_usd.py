# Generated by Django 2.2.1 on 2021-05-21 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_products_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='price_usd',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
