# Generated by Django 4.1 on 2022-08-28 19:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schematics', '0011_alter_schematics_currentdatetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schematics',
            name='currentDateTime',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 28, 19, 43, 28, 988225, tzinfo=datetime.timezone.utc)),
        ),
    ]