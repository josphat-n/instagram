# Generated by Django 2.1 on 2020-01-06 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0005_auto_20200106_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_profile',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='insta.Profile'),
        ),
    ]
