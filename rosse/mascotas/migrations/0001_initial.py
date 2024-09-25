# Generated by Django 5.1.1 on 2024-09-24 17:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('especie', models.CharField(max_length=15)),
                ('raza', models.CharField(max_length=50)),
                ('notas', models.TextField(blank=True, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
            ],
            options={
                'verbose_name': 'Mascota',
                'verbose_name_plural': 'Mascotas',
                'db_table': 'mascotas',
            },
        ),
    ]
