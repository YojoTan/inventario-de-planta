# Generated by Django 4.1.7 on 2023-02-28 02:05

import app_inventario.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='articulo_has_empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.PositiveSmallIntegerField(default=5, verbose_name=app_inventario.models.Empleado)),
                ('idArticulo', models.PositiveSmallIntegerField(default=5, verbose_name=app_inventario.models.Articulo)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCategoria', models.PositiveSmallIntegerField(default=10)),
                ('nomCategoria', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('nit', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nomEmpresa', models.CharField(max_length=45)),
                ('direccion', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('documento', models.PositiveSmallIntegerField(default=5, primary_key=True, serialize=False)),
                ('nomEmpleado', models.CharField(max_length=45)),
                ('apellidos', models.CharField(max_length=45)),
                ('telefono', models.PositiveSmallIntegerField(default=5)),
                ('e_mail', models.CharField(max_length=45)),
                ('idEmpresa', models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='app_inventario.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idArticulo', models.PositiveSmallIntegerField(default=10)),
                ('nomArticulo', models.CharField(max_length=45)),
                ('cantidad', models.PositiveSmallIntegerField(default=10)),
                ('idCategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_inventario.categoria')),
            ],
        ),
    ]
