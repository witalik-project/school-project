# Generated by Django 4.1.1 on 2022-10-26 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0036_alter_classes_class_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointslog',
            name='points_log_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]