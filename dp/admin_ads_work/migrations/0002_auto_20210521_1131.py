# Generated by Django 2.2.1 on 2021-05-21 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_ads_work', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaigns',
            name='fast_link_yand',
            field=models.CharField(blank=True, max_length=71, null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='fast_link_yand_desc',
            field=models.CharField(blank=True, max_length=240, null=True),
        ),
    ]
