# Generated by Django 3.0.2 on 2020-04-13 03:35

import datetime
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200412_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tutorAvailability',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.DateTimeField(blank=True, default=datetime.datetime.now), blank=True, default=list, size=None),
        ),
    ]
