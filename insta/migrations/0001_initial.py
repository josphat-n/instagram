# Generated by Django 2.2 on 2020-01-04 18:42

from django.db import migrations, models
import django.db.models.deletion
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', pyuploadcare.dj.models.ImageField(blank=True)),
                ('bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=30)),
                ('image_image', pyuploadcare.dj.models.ImageField(blank=True)),
                ('image_caption', models.TextField()),
                ('image_likes', models.IntegerField()),
                ('image_comments', models.TextField()),
                ('image_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insta.Profile')),
            ],
        ),
    ]