# Generated by Django 3.1 on 2020-08-04 16:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20200804_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logement',
            name='id',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='id',
        ),
        migrations.AddField(
            model_name='logement',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, help_text='Identifiant unique pour ce logement', primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='reservation',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, help_text='Identifiant unique pour cette reservation', primary_key=True, serialize=False),
        ),
    ]
