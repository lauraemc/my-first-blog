# Generated by Django 2.2.13 on 2020-08-31 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200831_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extra',
            name='author',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='author',
        ),
        migrations.RemoveField(
            model_name='workelement',
            name='author',
        ),
    ]
