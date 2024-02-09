# Generated by Django 5.0.1 on 2024-01-20 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_usuarios_direccion_pedidos'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidos',
            name='abono',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='detalle',
            field=models.CharField(default=100, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedidos',
            name='entregado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='medida',
            field=models.CharField(default=100, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedidos',
            name='por_pagar',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='pedidos',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]