# Generated by Django 4.1.1 on 2022-10-03 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0033_remove_subtractpointslog_points_subtract_log_class_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointslog',
            name='points_log_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
