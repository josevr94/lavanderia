# Generated by Django 5.1.3 on 2024-11-20 15:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
        ('empleado', '0001_initial'),
        ('prendas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdenDeServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('Recibido', 'Recibido'), ('En Proceso', 'En Proceso'), ('Completado', 'Completado'), ('Entregado', 'Entregado')], default='Recibido', max_length=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleado.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='PrendaOrden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordendeservicio.ordendeservicio')),
                ('prenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prendas.prenda')),
            ],
        ),
        migrations.AddField(
            model_name='ordendeservicio',
            name='prendas',
            field=models.ManyToManyField(through='ordendeservicio.PrendaOrden', to='prendas.prenda'),
        ),
    ]
