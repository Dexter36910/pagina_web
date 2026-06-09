from django.db import models

class Usuario(models.Model):
    usuario = models.CharField(max_length=50, unique=True)
    edad = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=100)
    opinion = models.TextField(blank=True)

    def __str__(self):
        return self.usuario