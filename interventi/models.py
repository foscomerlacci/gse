from django.db import models
from dispositivi.models import Dispositivo
from anagrafica.models import Utente
from django.core.exceptions import ValidationError
from datetime import date
from django.contrib.auth.models import User

# today = date.today()

# Create your models here.

############################################ metodi validatori ###############################

def valida_data_richiesta(value):
    if value > date.today():
        raise ValidationError('la data di richiesta intervento non può essere nel futuro')

def valida_data_chiusura(value):
    if value > date.today():
        raise ValidationError('la data di chiusura intervento non può essere nel futuro')

################################################################################################

###### funzioncina fondamentale per l'override del metodo __str__ dell'AUTH_USER_MODEL  ##############

def get_full_name(self):
    return self.first_name + " " + self.last_name

User.add_to_class('__str__', get_full_name)

#####################################################################################################


class Intervento(models.Model):

    scelte_tipo_ticket = (
        ('incident', 'incident'),
        ('IMAC', 'IMAC'),
        ('change', 'change'),
        ('move', 'move'),
        ('altro', 'altro'),
    )

    scelte_stato_intervento = (
        ('chiuso', 'chiuso'),
        ('counter stop', 'counter stop'),
        ('cancelled', 'cancelled'),
    )

    scelte_tipo_ingaggio = (
        ('mail Coppetta', 'mail Coppetta'),
        ('telefonata Coppetta', 'telefonata Coppetta'),
        ('telefonata utente', 'telefonata utente'),
    )

    scelte_area_intervento = (
        ('User Management', 'User Management'),
        ('PC SW', 'PC SW'),
        ('PC HW', 'PC HW'),
        ('Mobile', 'Mobile'),
        ('Messaging', 'Messaging'),
        ('Video/Audio comunicazione', 'Video/Audio comunicazione'),
        ('Aree condivise', 'Aree condivise'),
        ('Backup/ripristino', 'Backup/ripristino'),
        ('Applicativi', 'Applicativi'),
        ('Sicurezza', 'Sicurezza'),
        ('Informazioni/procedure', 'Informazioni/procedure'),
        ('Printing', 'Printing'),
        ('Move', 'Move'),
    )


    tecnico = models.CharField(max_length=40, null=True )
    tipo_servizio = models.CharField(max_length=20, default="ENHANCED",)
    richiedente = models.CharField(max_length=20, default="ROSSELLA MACCHI")
    data_richiesta = models.DateField(null=False, blank=False, validators=[valida_data_richiesta])
    data_chiusura = models.DateField(null=False, blank=False, validators=[valida_data_chiusura])
    fk_beneficiario = models.ForeignKey('anagrafica.Utente', verbose_name='beneficiario', on_delete=models.CASCADE, null=False)
    asset = models.ForeignKey('dispositivi.Dispositivo', verbose_name='dispositivo', on_delete=models.CASCADE, blank=True, null=True)
    tipo_ticket = models.CharField(max_length=30, choices=scelte_tipo_ticket, null=False, blank=False)
    numero_ticket = models.CharField(max_length=10, null=True, blank=True)
    area_intervento = models.CharField(max_length=30, choices=scelte_area_intervento, null=False, blank=False)
    descrizione_richiesta = models.TextField(max_length=300, null=False, blank=False )
    soluzione_adottata = models.TextField(max_length=300, null=False, blank=False)
    stato_intervento = models.CharField(max_length=30, choices=scelte_stato_intervento, null=False, blank=False)
    tipo_ingaggio = models.CharField(max_length=30, choices=scelte_tipo_ingaggio, null=False, blank=False)
    note = models.TextField(max_length=300, null=True, blank=True )


    def __str__(self):
        return str(self.pk)
        # return self.fk_beneficiario.cognome + " -- " + self.asset.asset + " -- " + self.asset.modello

    class Meta:
        verbose_name_plural = 'interventi'