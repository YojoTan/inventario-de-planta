# Generated by Django 4.1.7 on 2023-02-28 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_inventario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='idArticulo',
            field=models.PositiveSmallIntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='idCategoria',
            field=models.PositiveSmallIntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='documento',
            field=models.PositiveSmallIntegerField(primary_key=True, serialize=False, verbose_name='documento'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='nit',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='nit'),
        ),
    ]