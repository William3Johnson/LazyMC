# Generated by Django 4.1 on 2022-08-28 11:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schematics', '0004_remove_schematics_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='schematics',
            name='currentDateTime',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 28, 11, 18, 43, 186034)),
        ),
    ]
