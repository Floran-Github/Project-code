# Generated by Django 3.0.7 on 2020-12-31 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_auto_20200912_0210'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': 'Department', 'verbose_name_plural': 'Departments'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={},
        ),
    ]