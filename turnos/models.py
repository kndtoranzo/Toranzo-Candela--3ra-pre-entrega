from django.db import models


class Turnos(models.Model):
    fecha = models.DateField()
    tipo_manicura = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=300)
    
    def __str__(self):
        return f"{self.tipo_manicura} - {self.fecha}"