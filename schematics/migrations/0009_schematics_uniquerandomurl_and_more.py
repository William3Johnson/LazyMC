# Generated by Django 4.1 on 2022-08-28 16:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schematics', '0008_schematics_filelink_alter_schematics_currentdatetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='schematics',
            name='uniqueRandomURL',
            field=models.CharField(default=8794306359, editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='schematics',
            name='currentDateTime',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 28, 16, 55, 38, 283899, tzinfo=datetime.timezone.utc)),
        ),
    ]