# Generated by Django 3.1 on 2020-08-04 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20200804_1847'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logement',
            options={},
        ),
        migrations.AlterModelOptions(
            name='reservation',
            options={},
        ),
        migrations.RemoveField(
            model_name='logement',
            name='capacite',
        ),
        migrations.RemoveField(
            model_name='logement',
            name='nom',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='debut',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='fin',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='logement',
        ),
    ]
