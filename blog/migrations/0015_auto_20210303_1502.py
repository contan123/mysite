# Generated by Django 3.1.2 on 2021-03-03 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20210303_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='urls',
            field=models.URLField(blank=True, default='#'),
        ),
    ]
