# Generated by Django 5.1.1 on 2024-09-24 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='dni',
            field=models.CharField(max_length=8, unique=True),
        ),
    ]
