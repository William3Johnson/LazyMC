# Generated by Django 4.1 on 2022-08-30 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schematics', '0016_alter_schematics_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schematics',
            name='category',
        ),
        migrations.AlterField(
            model_name='schematics',
            name='description',
            field=models.TextField(help_text='The actual description shown in the dedicated page for the schematic'),
        ),
        migrations.DeleteModel(
            name='categorySelect',
        ),
    ]
