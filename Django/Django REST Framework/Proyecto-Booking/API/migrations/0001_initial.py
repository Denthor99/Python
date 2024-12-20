# Generated by Django 5.0.7 on 2024-07-29 17:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='nombre')),
                ('description', models.TextField(blank=True, max_length=255, null=True, verbose_name='descripción')),
                ('type', models.CharField(choices=[('HU', 'Humano'), ('FI', 'Financiero'), ('MA', 'Material'), ('TE', 'Técnico')], default='MA', max_length=2, verbose_name='Tipo de recurso')),
            ],
            options={
                'verbose_name': 'Recurso',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Fecha de inicio')),
                ('end_date', models.DateField(verbose_name='Fecha de fin')),
                ('start_time', models.TimeField(verbose_name='Hora de inicio')),
                ('end_time', models.TimeField(verbose_name='Hora de fin')),
                ('status', models.CharField(choices=[('SO', 'Solicitado'), ('CO', 'Concedido'), ('US', 'En uso'), ('FI', 'Finalizado')], default='SO', max_length=2, verbose_name='Estado del recurso')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.resource', verbose_name='Recurso')),
            ],
            options={
                'verbose_name': 'Reserva',
                'order_with_respect_to': 'user',
            },
        ),
    ]
