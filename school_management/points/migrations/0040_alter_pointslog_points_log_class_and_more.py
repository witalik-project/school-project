# Generated by Django 4.1.1 on 2022-11-01 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0039_alter_pointslog_points_log_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointslog',
            name='points_log_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='points.classes'),
        ),
        migrations.AlterField(
            model_name='pointslog',
            name='points_log_type',
            field=models.CharField(choices=[(True, 'Add'), (False, 'No')], max_length=5, null=True),
        ),
    ]
