# Generated by Django 4.1.1 on 2022-11-01 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0038_remove_classes_class_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointslog',
            name='points_log_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
