# Generated by Django 4.1.1 on 2022-10-03 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0029_alter_classes_class_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointslog',
            name='points_log_type',
            field=models.BooleanField(),
        ),
    ]
