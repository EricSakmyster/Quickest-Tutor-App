# Generated by Django 3.0.2 on 2020-04-05 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200405_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
