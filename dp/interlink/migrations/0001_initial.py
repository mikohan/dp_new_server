# Generated by Django 2.2.1 on 2019-10-09 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tableredirectcat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_old', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=70, null=True)),
                ('id_new', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
