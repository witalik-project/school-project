# Generated by Django 4.1.5 on 2023-05-01 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0048_alter_classes_class_school_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='class_school_level',
            field=models.CharField(choices=[('Klasy początkowe', 'Klasy początkowe'), ('Klasy średnie', 'Klasy średnie'), ('Klasy starsze', 'Klasy starsze')], default='Klasy średnie', max_length=16, verbose_name='Poziom szkolnictwa'),
        ),
    ]