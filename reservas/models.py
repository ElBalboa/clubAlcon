from django.db import models
from django.contrib.auth.models import User


class Usuario(User):
    # campos personalizados si querés
    es_socio = models.BooleanField(default=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username

class Reserva(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    cancha = models.CharField(max_length=50)
    estado = models.CharField(max_length=20, choices=[("pendiente", "Pendiente"), ("confirmada", "Confirmada"), ("cancelada", "Cancelada")])
