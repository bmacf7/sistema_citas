# Generated by Django 5.1.1 on 2024-09-24 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='email',
            new_name='correo',
        ),
    ]
