from django.db import models


class manicura (models.Model):
    modelo = models.CharField( max_length=20)
    largo = models.CharField( max_length=20)
    color = models.CharField( max_length=20)

    
    