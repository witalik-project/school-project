# Generated by Django 4.1.5 on 2023-03-15 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0045_alter_pointslog_points_log_type'),
        ('tournaments', '0008_tournamentbattle_battle_second_oponent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournamentbattle',
            name='battle_first_oponent',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='first_oponent', to='points.classes'),
        ),
        migrations.AlterField(
            model_name='tournamentbattle',
            name='battle_second_oponent',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_oponent', to='points.classes'),
        ),
    ]