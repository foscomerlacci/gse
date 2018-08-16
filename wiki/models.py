from django.db import models

# Create your models here.

class Contatto(models.Model):
    servizio = models.CharField(max_length=100)
    nome = models.CharField(max_length=50, blank=True)
    cognome = models.CharField(max_length=50 , blank=True)
    area = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    note = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return str(self.servizio)

    class Meta:
        verbose_name_plural = 'contatti'
        ordering = ['servizio',]