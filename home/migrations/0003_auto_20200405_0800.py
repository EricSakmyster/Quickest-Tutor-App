# Generated by Django 3.0.3 on 2020-04-05 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200405_0231'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='majors',
            field=models.TextField(default='none', max_length=500),
        ),
        migrations.AddField(
            model_name='student',
            name='pn',
            field=models.CharField(default='0000000000', max_length=10),
        ),
        migrations.AddField(
            model_name='student',
            name='subjects',
            field=models.TextField(default='none', max_length=500),
        ),
    ]
