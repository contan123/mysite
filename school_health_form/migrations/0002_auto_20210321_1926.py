# Generated by Django 3.1.2 on 2021-03-21 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_health_form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthinfo',
            name='password',
            field=models.CharField(max_length=2000),
        ),
    ]
