# Generated by Django 3.0.5 on 2021-05-28 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='year_in_school',
            field=models.CharField(choices=[('FOND', 'Licence Fondamentale'), ('APP', 'Licence Appliquée'), ('MAR', 'Master de Recherche'), ('MAP', 'Master Professionel')], default='FOND', max_length=5),
        ),
    ]
