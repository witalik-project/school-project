# Generated by Django 4.1.1 on 2022-11-01 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0040_alter_pointslog_points_log_class_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointslog',
            name='points_log_type',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
