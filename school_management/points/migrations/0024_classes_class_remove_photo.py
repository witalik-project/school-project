# Generated by Django 4.1.1 on 2022-10-02 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0023_alter_classes_class_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='class_remove_photo',
            field=models.BooleanField(null=True),
        ),
    ]
