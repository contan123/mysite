# Generated by Django 3.1.2 on 2021-03-18 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HealthInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4)),
                ('username', models.TextField()),
                ('password', models.CharField(max_length=20)),
                ('FDY', models.CharField(max_length=4)),
                ('SSH', models.CharField(max_length=20)),
                ('XY', models.CharField(max_length=20)),
                ('BJ', models.CharField(max_length=20)),
            ],
        ),
    ]
