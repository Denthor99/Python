from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(null=True, blank=True, verbose_name="Descripción")
    complete = models.BooleanField(default=False, verbose_name="Completado")
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title