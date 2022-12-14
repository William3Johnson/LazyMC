# Generated by Django 4.1 on 2022-08-29 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schematics', '0014_alter_schematics_currentdatetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='categorySelect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=154, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='schematics',
            name='category',
        ),
        migrations.AddField(
            model_name='schematics',
            name='category',
            field=models.ManyToManyField(to='schematics.categoryselect'),
        ),
    ]
