# Generated by Django 2.2.1 on 2021-05-21 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20210521_1707'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='price',
            new_name='_price',
        ),
    ]
