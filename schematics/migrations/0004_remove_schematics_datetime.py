# Generated by Django 4.1 on 2022-08-28 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schematics', '0003_schematics_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schematics',
            name='dateTime',
        ),
    ]
