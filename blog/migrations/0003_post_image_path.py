# Generated by Django 2.2.13 on 2020-08-27 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_text_preview'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_path',
            field=models.TextField(blank=True),
        ),
    ]