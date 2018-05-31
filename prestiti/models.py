from django.db import models
from django.shortcuts import render

from anagrafica.models import Utente
from django.conf import settings
from django.db import connection
from django.db.models import signals
from crequest.middleware import CrequestMiddleware
from django.contrib.auth.models import User

# from .middlewares.middlewares import  RequestMiddleware
# from django.http import request
# import requests
from django.core.exceptions import ValidationError
from datetime import date, datetime
import datetime
from datetime import datetime
from django.utils import timezone as tz
import pytz


today = date.today()
# now = datetime.datetime.now(pytz.timezone('Europe/Rome'))
# now = datetime.now()
now = tz.now()


############################################### metodi validatori ############################
def valida_data_checkin(value):
    if value > today:
        raise ValidationError('la data di checkin non può essere nel futuro')

def valida_data_checkout(value):
    if value > today:
        raise ValidationError('la data di checkout non può essere nel futuro')

def valida_fine_garanzia(value):
    if value < today:
        raise ValidationError('la fine della garanzia non può essere nel passato')

def valida_inizio_prestito(value):
    if value > now:
        raise ValidationError('il prestito non può iniziare nel futuro')
#     pass

def valida_fine_prestito(value):
    if value > now:
        raise ValidationError('il prestito non può terminare nel futuro')
#     pass

###############################################################################################

# Create your models here.

###### funzioncina fondamentale per l'override del metodo __str__ dell'AUTH_USER_MODEL  ##############

def get_full_name(self):
    return self.first_name + " " + self.last_name

User.add_to_class('__str__', get_full_name)

#####################################################################################################



class Prestiti_Dispositivo(models.Model):

    # scelte_device = (
    #     ('des', 'desktop'),
    #     ('lap', 'laptop'),
    #     ('tab', 'tablet'),
    #     ('sma', 'smartphone'),
    #     ('sta', 'stampante'),
    #     ('doc', 'docking'),
    #     ('mon', 'monitor'),
    # )

    scelte_location = (
        ('Roma - Laurentina', 'Roma - Laurentina'),
        ('Roma - Mattei', 'Roma - Mattei'),
        ('Milano - SDM', 'Milano - SDM'),
    )

    asset = models.CharField(max_length=10, unique=True)
    # location= models.CharField(max_length=30, choices=scelte_location, default= scelte_location[0])
    # palazzo = models.CharField(max_length=20, null=True, blank=True)
    # piano = models.CharField(max_length=10, null=True, blank=True)
    # stanza = models.CharField(max_length=3, null=True, blank=True)
    tipo_dispositivo = models.ForeignKey('prestiti.Prestiti_Tipo_Dispositivo', verbose_name='tipo dispositivo', on_delete=models.CASCADE)
    produttore = models.ForeignKey('prestiti.Prestiti_Produttore', verbose_name='produttore', on_delete=models.CASCADE)
    modello = models.ForeignKey('prestiti.Prestiti_Modello', verbose_name='modello', on_delete=models.CASCADE)
    # tipo_dispositivo = models.CharField(max_length=3, choices=scelte_device, default=scelte_device[0])
    seriale = models.CharField(max_length=30, unique=True)
    data_checkin = models.DateField(validators=[valida_data_checkin])
    data_checkout = models.DateField(null=True, blank=True, validators=[valida_data_checkout])
    fine_garanzia = models.DateField(null=True, blank=True, validators=[valida_fine_garanzia])
    # produttore = models.CharField(max_length=20)
    # modello = models.CharField(max_length=20)
    os = models.CharField(max_length= 15, verbose_name='O.S', null=True, blank=True)
    # utente = models.ForeignKey('anagrafica.Utente', verbose_name='assegnatario', on_delete=models.CASCADE,)
    note = models.TextField(max_length=500, null=True, blank=True)
    disponibile = models.BooleanField(default=True)
    # allegati = models.FileField(upload_to='static', null=True, blank=True)


    def __str__(self):
        # return str(self.tipo_dispositivo) + " " + str(self.modello)
        return  str(self.tipo_dispositivo) + " | " + str(self.modello) + " | " + str(self.asset)

    class Meta:
        verbose_name = 'dispositivo'
        verbose_name_plural = 'dispositivi'
        # app_label = 'Prestiti_Dispositivo'




class Prestiti_Tipo_Dispositivo(models.Model):
    tipo_dispositivo = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return str(self.tipo_dispositivo)

    class Meta:
        verbose_name_plural = 'tipi dispositivo'
        verbose_name = 'tipo dispositivo'
        ordering = ['tipo_dispositivo']


class Prestiti_Produttore(models.Model):
    produttore = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return str(self.produttore)

    class Meta:
        verbose_name_plural = 'produttori'
        verbose_name = 'produttore'
        ordering = ['produttore']


class Prestiti_Modello(models.Model):
    fk_tipo_dispositivo = models.ForeignKey(Prestiti_Tipo_Dispositivo, verbose_name='tipo dispositivo', null=False, on_delete=models.CASCADE)
    fk_produttore = models.ForeignKey(Prestiti_Produttore, verbose_name='produttore', null=False, on_delete=models.CASCADE)
    modello = models.CharField(max_length=30, unique=True,)
    attivo = models.BooleanField(default=True)



    def __str__(self):
        return str(self.modello)

    class Meta:
        verbose_name_plural = 'modelli'
        verbose_name = 'modello'
        ordering = ['modello']


class Prestito(models.Model):
    fk_utente = models.ForeignKey('anagrafica.Utente', verbose_name='assegnatario', null=False, on_delete=models.CASCADE)
    fk_dispositivo = models.ForeignKey('prestiti.Prestiti_Dispositivo', verbose_name='dispositivo', null=False, on_delete=models.CASCADE)
    inizio_prestito = models.DateTimeField(null=False, blank=False, )
    fine_prestito = models.DateTimeField(null=True, blank=True, )
    tecnico_consegna = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tecnico_consegna', null=False, on_delete=models.CASCADE)
    tecnico_ritiro = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tecnico_ritiro', null=True, blank=True, on_delete=models.CASCADE)
    note = models.TextField(max_length=500, null=True, blank=True)

    # def clean_tecnico_consegna(self):
    #     tecnico_consegna = self.cleaned_data['tecnico_consegna']
    #     tecnico_consegna = tecnico_consegna.replace('.', ' ')  # sostituisce il punto con lo spazio
    #     return tecnico_consegna


    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = 'prestiti'
        verbose_name = 'prestito'
        ordering = ['inizio_prestito']


class Prestiti_Allegato(models.Model):
    prestito = models.ForeignKey(Prestito, on_delete=models.CASCADE)
    descrizione = models.CharField(max_length=30, null=True, blank=True)
    allegato = models.FileField()
    inserito_il = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.allegato)

    class Meta:
        verbose_name_plural = 'allegati'
        verbose_name = 'allegato'



def agg_disponibile(sender, instance, created, **kwargs):

    # d = int(exposed_request.POST['fk_dispositivo'])
    # from crequest.middleware import CrequestMiddleware

    current_request = CrequestMiddleware.get_request()
    cr = int(current_request.POST.__getitem__('fk_dispositivo'))
    fp_0 = current_request.POST.__getitem__('fine_prestito_0')
    fp_1 = current_request.POST.__getitem__('fine_prestito_1')
    cursor = connection.cursor()

    if fp_0 == '':
        cursor.execute('''UPDATE prestiti_prestiti_dispositivo SET disponibile = 0 WHERE prestiti_prestiti_dispositivo.id = %s ''', [cr])
    else:
        cursor.execute('''UPDATE prestiti_prestiti_dispositivo SET disponibile = 1 WHERE prestiti_prestiti_dispositivo.id = %s''',[cr])


    # cursor.execute('''UPDATE prestiti_prestiti_dispositivo SET disponibile = 0 WHERE prestiti_prestiti_dispositivo.id = %s ''',[cr])

signals.post_save.connect(agg_disponibile, sender = Prestito,)