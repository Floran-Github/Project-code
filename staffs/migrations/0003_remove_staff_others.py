# Generated by Django 3.0.7 on 2020-08-17 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staffs', '0002_auto_20200817_2319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='others',
        ),
    ]
