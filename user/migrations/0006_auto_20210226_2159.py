# Generated by Django 3.1.2 on 2021-02-26 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_profile_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Avatar',
        ),
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatar/'),
        ),
    ]