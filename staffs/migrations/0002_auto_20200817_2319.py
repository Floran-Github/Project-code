# Generated by Django 3.0.7 on 2020-08-17 17:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
        ('staffs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='date_of_admission',
            new_name='date_of_join',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='other_name',
        ),
        migrations.AddField(
            model_name='staff',
            name='Subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.Subject'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='current_status',
            field=models.CharField(choices=[('assistant', 'Assistant'), ('lecturer', 'Lecturer')], default='active', max_length=10),
        ),
        migrations.AlterField(
            model_name='staff',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator(message="Entered mobile number isn't in a right format!", regex='^[0-9]{10,15}$')]),
        ),
    ]
