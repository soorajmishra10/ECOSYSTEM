# Generated by Django 2.1.7 on 2019-04-27 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile_feed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='user_image',
            field=models.ImageField(blank=True, default='pf-icon1.png', upload_to='profile_images'),
        ),
    ]
