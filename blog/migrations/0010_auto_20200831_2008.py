# Generated by Django 2.2.13 on 2020-08-31 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200830_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workelement',
            name='paid',
            field=models.BooleanField(blank=True),
        ),
    ]