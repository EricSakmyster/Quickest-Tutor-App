# Generated by Django 3.0.2 on 2020-04-13 02:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200412_2207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='tutorAvailibility',
            new_name='tutorAvailability',
        ),
    ]
