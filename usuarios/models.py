from django.db import models

class Registro(models.Model):
    username = models.CharField( max_length=20)
    email = models.CharField( max_length=20)

    def __str__(self):
        return self.username
