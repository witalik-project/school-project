# Generated by Django 4.1.5 on 2023-03-13 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0004_tournamentbattle_battle_first_oponent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournamentbattle',
            name='battle_first_oponent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tournaments.tournament'),
        ),
    ]