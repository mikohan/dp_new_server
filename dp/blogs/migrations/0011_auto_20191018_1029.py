# Generated by Django 2.2.6 on 2019-10-18 07:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0010_auto_20191017_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oldblogs',
            name='publish',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
