from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
from django.contrib.auth.models import User

today = date.today()

############################################### metodi validatori ############################
def valida_data_installazione(value):
    if value > today:
        raise ValidationError('la data di installazione non può essere nel futuro')

def valida_data_dismissione(value):
    if value > today:
        raise ValidationError('la data di dismissione non può essere nel futuro')

def valida_fine_garanzia(value):
    if value < today:
        raise ValidationError('la fine della garanzia non può essere nel passato')

###############################################################################################

################################################################################################

###### funzioncina fondamentale per l'override del metodo __str__ dell'AUTH_USER_MODEL  ##############

def get_full_name(self):
    return self.first_name + " " + self.last_name

User.add_to_class('__str__', get_full_name)

#####################################################################################################

# Create your models here.

class Dispositivo(models.Model):

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
    location= models.CharField(max_length=30, choices=scelte_location, default= scelte_location[0])
    palazzo = models.CharField(max_length=20, null=True, blank=True)
    piano = models.CharField(max_length=10, null=True, blank=True)
    stanza = models.CharField(max_length=3, null=True, blank=True)
    tipo_dispositivo = models.ForeignKey('dispositivi.Tipo_Dispositivo', verbose_name='tipo dispositivo', on_delete=models.CASCADE)
    produttore = models.ForeignKey('dispositivi.Produttore', verbose_name='produttore', on_delete=models.CASCADE)
    modello = models.ForeignKey('dispositivi.Modello', verbose_name='modello', on_delete=models.CASCADE)
    # tipo_dispositivo = models.CharField(max_length=3, choices=scelte_device, default=scelte_device[0])
    seriale = models.CharField(max_length=30, unique=True)
    data_installazione = models.DateField(validators=[valida_data_installazione])
    data_dismissione = models.DateField(null=True, blank=True, validators=[valida_data_dismissione])
    fine_garanzia = models.DateField(null=True, blank=True, validators=[valida_fine_garanzia])
    # produttore = models.CharField(max_length=20)
    # modello = models.CharField(max_length=20)
    os = models.CharField(max_length= 15, verbose_name='O.S', null=True, blank=True)
    utente = models.ForeignKey('anagrafica.Utente', verbose_name='assegnatario', on_delete=models.CASCADE,)
    note = models.TextField(max_length=200, null=True, blank=True)
    # allegati = models.FileField(upload_to='static', null=True, blank=True)


    def __str__(self):
        # return str(self.tipo_dispositivo) + " " + str(self.modello)
        return self.asset

    class Meta:
        verbose_name_plural = 'dispositivi'


class Allegato(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    descrizione = models.CharField(max_length=30, null=True, blank=True)
    allegato = models.FileField()
    inserito_il = models.DateField(auto_now_add= True)

    def __str__(self):
        return str(self.allegato)

    class Meta:
        verbose_name_plural = 'allegati'
        verbose_name = 'allegato'



class Tipo_Dispositivo(models.Model):
    tipo_dispositivo = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return str(self.tipo_dispositivo)

    class Meta:
        verbose_name_plural = 'tipi dispositivo'
        verbose_name = 'dispositivo'
        ordering = ['tipo_dispositivo']


class Produttore(models.Model):
    produttore = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return str(self.produttore)

    class Meta:
        verbose_name_plural = 'produttori'
        verbose_name = 'produttore'
        ordering = ['produttore']


class Modello(models.Model):
    fk_tipo_dispositivo = models.ForeignKey(Tipo_Dispositivo, verbose_name='tipo dispositivo', null=False, on_delete=models.CASCADE)
    fk_produttore = models.ForeignKey(Produttore, verbose_name='produttore', null=False, on_delete=models.CASCADE)
    modello = models.CharField(max_length=30, unique=True,)
    attivo = models.BooleanField(default=True)



    def __str__(self):
        return str(self.modello)

    class Meta:
        verbose_name_plural = 'modelli'
        verbose_name = 'modello'
        ordering = ['modello']