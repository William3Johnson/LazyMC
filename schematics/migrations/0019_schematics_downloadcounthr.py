# Generated by Django 4.1 on 2022-08-30 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schematics', '0018_schematics_downloadcount'),
    ]

    operations = [
        migrations.AddField(
            model_name='schematics',
            name='downloadCountHR',
            field=models.CharField(default=0, editable=False, max_length=128),
        ),
    ]