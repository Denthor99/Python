from django.db import models
from django.contrib.auth.models import User

class Resource(models.Model):
    class Meta:
        verbose_name = 'Recurso'

    RESOURCE_TYPE = [
        ('HU', 'Humano'),
        ('FI', 'Financiero'),
        ('MA', 'Material'),
        ('TE', 'Técnico'),
    ]
    name = models.CharField(max_length=50, verbose_name="nombre")
    description = models.TextField(max_length=255, verbose_name="descripción", null=True, blank=True)
    type = models.CharField(max_length=2, choices=RESOURCE_TYPE, default='MA', verbose_name="Tipo de recurso")

    def __str__(self):
        return f'{self.pk} - {self.name} - {self.description}'

class Booking(models.Model):
    class Meta:
        verbose_name = 'Reserva'
        order_with_respect_to = 'user'
    
    RESOURCE_TYPE = [
        ('SO', 'Solicitado'),
        ('CO', 'Concedido'),
        ('US', 'En uso'),
        ('FI', 'Finalizado'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, verbose_name="Recurso")
    start_date = models.DateField(verbose_name="Fecha de inicio")
    end_date = models.DateField(verbose_name="Fecha de fin")
    start_time = models.TimeField(verbose_name='Hora de inicio')
    end_time = models.TimeField(verbose_name='Hora de fin')
    status = models.CharField(max_length=2, choices=RESOURCE_TYPE, default='SO', verbose_name='Estado del recurso')

    def __str__(self):
        return f'{self.pk} - {self.user} - {self.resource}'