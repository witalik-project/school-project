# Generated by Django 4.1.1 on 2022-10-02 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0020_alter_classes_class_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='class_photo',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='images'),
        ),
    ]