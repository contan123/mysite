# Generated by Django 3.1.2 on 2021-02-18 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('read_statistics', '0002_readdetail'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogReadNum',
        ),
    ]
