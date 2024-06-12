from django.db import models


class manicura (models.Model):
    modelo = models.CharField( max_length=20)
    largo = models.CharField( max_length=20)
    color = models.CharField( max_length=20)

    def _str_(self):
        return f"{self.modelo} - {self.largo} - {self.color}"
    