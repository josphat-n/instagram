# Generated by Django 2.1 on 2020-01-06 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_profile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_comments',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_likes',
            field=models.IntegerField(blank=True),
        ),
    ]