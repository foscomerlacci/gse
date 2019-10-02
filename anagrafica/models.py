from django.db import models
from django.utils.translation import ugettext_lazy as _



# Create your models here.


class Utente(models.Model):
    # scelte_user_type = (
    #     ('fas', 'fast'),
    #     ('enh', 'enhanced'),
    # )
    scelte_ruolo = (
        ('dir', 'dirigenza'),
        ('seg', 'segreteria'),
    )

    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)
    matricola = models.CharField(max_length=10, unique=True)
    utenza = models.CharField(max_length=10, unique=True)
    divisione = models.CharField(max_length=50, null=True, blank=True)
    # user_type = models.CharField(max_length=3, choices=scelte_user_type, default=scelte_user_type[1])
    ruolo = models.CharField(max_length=3, choices=scelte_ruolo, default=scelte_ruolo[0])
    segretaria_associata = models.ManyToManyField("self", blank=True)
    # segretaria_associata = models.ManyToManyField("self", blank=True, through= 'Associazione', symmetrical=False)
    attivo = models.BooleanField(default=True)

    def __str__(self):
        # return str(self.cognome).capitalize() + " " + str(self.nome).capitalize()
        return str(self.cognome) + " " + str(self.nome)

    # class Segretarie(models.Manager):
    #     def get_queryset(self):
    #         return super().get_queryset().filter(ruolo = 'seg', attivo = True)


    class Meta:
        verbose_name_plural = 'utenti'
        ordering = ['cognome', '-attivo']



# class Associazione(models.Model):
#     types = models.ManyToManyField('Associazione', blank=True, related_name= 'utente_associazione')
#     from_utente_id = models.ForeignKey('Utente', related_name= 'from_utente')
#     to_utente_id = models.ForeignKey('Utente', related_name= 'to_utente')
#
#
#     class Meta:
#         unique_together = ('from_utente_id', 'to_utente_id')
