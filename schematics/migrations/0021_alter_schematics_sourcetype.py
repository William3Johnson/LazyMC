# Generated by Django 4.1 on 2022-08-30 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schematics', '0020_remove_schematics_source_schematics_sourcelink_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schematics',
            name='sourceType',
            field=models.CharField(choices=[('downloadedMap', 'Downloaded map and created schematic'), ('downloadedSchematic', 'Downloaded schematic directly')], default='downloadedSchematic', max_length=20),
        ),
    ]
