# Generated by Django 3.1.2 on 2020-12-01 00:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_producto', models.CharField(max_length=150, unique=True, verbose_name='Codigo Producto')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre Producto')),
                ('tipo', models.CharField(choices=[('fruta', 'Fruta'), ('verdura', 'Verdura'), ('pastas', 'Pastas'), ('bebidas', 'Bebidas'), ('bebidas Alcoholicas', 'Bebidas Alcoholicas'), ('utensilio', 'Utensilio'), ('carnes rojas', 'Carnes Rojas'), ('carnes blancas', 'Carnes Blancas'), ('arroz', 'Arroz'), ('postre', 'Postre'), ('lacteo', 'Lacteos'), ('pan', 'Pan'), ('condimento', 'Condimento'), ('bebedas', 'Bebidas')], max_length=30, null=True)),
                ('precio_Compra', models.PositiveSmallIntegerField(default=1, verbose_name='Precio de compra')),
                ('stock', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Stock')),
                ('gramaje', models.CharField(choices=[('ml', 'ML'), ('gr', 'Gr'), ('unidad', 'Unidad')], max_length=30, null=True)),
                ('descripcion', models.TextField(max_length=400, verbose_name='Descripcion del producto')),
            ],
            options={
                'db_table': 'Producto',
                'ordering': ['cod_producto'],
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10, null=True, unique=True)),
                ('nombre', models.CharField(max_length=120)),
                ('telefono', models.CharField(max_length=9, verbose_name='Teléfono')),
                ('direccion', models.CharField(max_length=200, verbose_name='Dirección')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedor',
                'db_table': 'Proveedor',
            },
        ),
        migrations.CreateModel(
            name='SolicitudProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(unique=True, verbose_name='Código Solicitud')),
                ('fecha_solicitud', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'SolicitudProducto',
            },
        ),
        migrations.CreateModel(
            name='IngresoPedidoProd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(unique=True, verbose_name='Código')),
                ('fecha_ingreso', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.proveedor')),
                ('solicitudProducto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='producto.solicitudproducto')),
            ],
            options={
                'db_table': 'IngresoPedido_prod',
            },
        ),
        migrations.CreateModel(
            name='FacturaPedidoProd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveSmallIntegerField(default=1, verbose_name='cantidad')),
                ('ingreso_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.ingresopedidoprod')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.producto')),
            ],
            options={
                'db_table': 'FacturaPedido_prod',
            },
        ),
        migrations.CreateModel(
            name='DetalleSolicitudProd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveSmallIntegerField(default=1, verbose_name='cantidad')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.producto')),
                ('solicitud_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.solicitudproducto')),
            ],
            options={
                'db_table': 'DetalleSolicitudProd',
            },
        ),
    ]
