# Generated by Django 4.1 on 2022-08-28 16:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schematics', '0007_alter_schematics_currentdatetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='schematics',
            name='fileLink',
            field=models.CharField(default='example link', help_text='link to the file for the schematic file', max_length=1024),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='schematics',
            name='currentDateTime',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 28, 16, 20, 11, 997382, tzinfo=datetime.timezone.utc)),
        ),
    ]