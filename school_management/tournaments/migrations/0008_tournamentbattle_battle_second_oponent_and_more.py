# Generated by Django 4.1.5 on 2023-03-15 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0045_alter_pointslog_points_log_type'),
        ('tournaments', '0007_tournamentbattle'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournamentbattle',
            name='battle_second_oponent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_oponent', to='points.classes'),
        ),
        migrations.AddField(
            model_name='tournamentbattle',
            name='winner',
            field=models.TextField(blank=True, choices=[('FT', 'First team'), ('ST', 'Second team')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='tournamentbattle',
            name='battle_first_oponent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='first_oponent', to='points.classes'),
        ),
    ]