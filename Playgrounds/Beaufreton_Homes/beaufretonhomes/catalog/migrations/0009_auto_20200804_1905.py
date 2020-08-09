# Generated by Django 3.1 on 2020-08-04 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20200804_1855'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logement',
            options={'ordering': ['nom']},
        ),
        migrations.AlterModelOptions(
            name='reservation',
            options={'ordering': ['debut', 'fin']},
        ),
        migrations.AddField(
            model_name='logement',
            name='capacite',
            field=models.IntegerField(default=0, help_text='Entre la capacité maximum du logement'),
        ),
        migrations.AddField(
            model_name='logement',
            name='nom',
            field=models.CharField(help_text='Entre le nom du logement', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='debut',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='fin',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='logement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.logement'),
        ),
    ]