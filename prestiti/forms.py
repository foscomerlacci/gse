from django import forms
from django.contrib.auth.models import User
from django.http import request
# from django_select2.forms import ModelSelect2Widget, Select2Widget
from django.http import HttpRequest
from django.db import connection
from django.db.models import signals
from django.http import request
from prestiti.fields import RestrictedFileField
from django.conf import settings
from prestiti.models import Prestito, Prestiti_Tipo_Dispositivo, Prestiti_Produttore, Prestiti_Modello, Prestiti_Dispositivo, Prestiti_Allegato
import pytz
from datetime import date, datetime
# import datetime


# today = date.today()
# now = datetime.datetime.now(pytz.timezone('Europe/Rome'))
# now = datetime.now()
# now = pytz.utc.localize(now)

tecnici_disponibili= forms.ModelChoiceField(queryset=User.objects.all().exclude(username='root').filter(is_active=True))


class PrestitoCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PrestitoCreateForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        # self.fields['tecnico_ritiro'].widget = forms.HiddenInput()
        # self.fields['fine_prestito'].widget = forms.HiddenInput()
        self.fields['tecnico_ritiro'].required = False
        self.fields['fine_prestito'].required = False
        # if instance and instance.id:

            # self.fields['fk_utente'].widget = forms.HiddenInput()
            # self.fields['fk_dispositivo'].widget = forms.HiddenInput()
            # self.fields['tecnico_consegna'].widget = forms.HiddenInput()
            # self.fields['inizio_prestito'].widget = forms.HiddenInput()

    fk_dispositivo = forms.ModelChoiceField(queryset= Prestiti_Dispositivo.objects.filter(disponibile="1").filter(data_checkout__isnull=True), label= "Dispositivo")
    tecnico_consegna = tecnici_disponibili


    note = forms.CharField(max_length=500, widget=forms.Textarea, required=False)


    def clean_inizio_prestito(self):           # metodo per la validazione del campo inizio_prestito
        inizio_prestito = self.cleaned_data['inizio_prestito']
        # inizio_prestito = inizio_prestito.replace(tzinfo=None)
        if inizio_prestito >= datetime.now():
            raise forms.ValidationError('il prestito non può iniziare nel futuro')

        return inizio_prestito


    class Media:
        js = (
            # '/static/popola_fk_dispositivo.js',
            # '/static/popola_asset.js',
            '/static/prestiti_hide_ritiro.js',
        )


    class Meta:
        model = Prestito

        fields = (

            'fk_utente',
            'fk_dispositivo',
            'tecnico_consegna',
            'inizio_prestito',
            'tecnico_ritiro',
            'fine_prestito',
            'note',
            )

        widgets = {
            # 'tecnico': forms.HiddenInput()

        }


class PrestitoChangeForm(forms.ModelForm):

    tecnico_ritiro = tecnici_disponibili

    def __init__(self, *args, **kwargs):
        super(PrestitoChangeForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields['tecnico_ritiro'].required = True
            self.fields['fine_prestito'].required = True
            # self.fields['fk_utente'].widget = forms.HiddenInput()
            # self.fields['fk_dispositivo'].widget = forms.HiddenInput()
            # self.fields['tecnico_consegna'].widget = forms.HiddenInput()
            # self.fields['inizio_prestito'].widget = forms.HiddenInput()

        note = forms.CharField(max_length=500, widget=forms.Textarea, required=False)

    def clean_fine_prestito(self):           # metodo per la validazione del campo fine_prestito
        fine_prestito = self.cleaned_data['fine_prestito']
        if fine_prestito <= self.cleaned_data['inizio_prestito']:
            raise forms.ValidationError(u'la data di fine prestito non può essere antecedente alla data di inizio')
        elif fine_prestito >= datetime.now():
            raise forms.ValidationError('il prestito non può terminare nel futuro')

        return fine_prestito


    class Media:
        js = (
            # '/static/popola_fk_dispositivo.js',
            # '/static/popola_asset.js',
            '/static/prestiti_hide_consegna.js',

        )


    class Meta:
        model = Prestito



        fields = (

            'fk_utente',
            'fk_dispositivo',
            'tecnico_consegna',
            'inizio_prestito',
            'tecnico_ritiro',
            'fine_prestito',
            'note',
            )



        widgets = {
            # 'fk_dispositivo': forms.HiddenInput()

        }


class Prestiti_AllegatoForm(forms.ModelForm):

    class Meta:
        model = Prestiti_Allegato
        fields = (
            'descrizione',
            'allegato',

        )
    allegato = RestrictedFileField(content_types=['application/pdf',
                                                  'text/plain',
                                                  'application/msword',
                                                  'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                                                  'application/vnd.ms-excel',
                                                  'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                                                  'image/jpeg',
                                                  'application/vnd.ms-outlook'],
                                    label= 'allegato')   # sovrascrivo l'etichetta del campo che fara' da intestazione





class Prestiti_DispositivoForm(forms.ModelForm):


    # def clean_tipo_dispositivo(self):                                   # metodo per normalizzare automaticamente l'input nella forma Xxxxxx
    #     return self.cleaned_data['tipo_dispositivo'].capitalize()

    # t = HttpRequest.POST.values()
    # t = HttpRequest.POST.get('bn')
    # def __init__(self, *args, **kwargs):
    #     super(DispositivoForm, self).__init__(*args, **kwargs)
    #     self.fields['produttore'].choices = list(Produttore.objects.values_list('id', 'produttore').filter())
    #     self.fields['modello'].choices = list(Modello.objects.values_list('id', 'modello'))
    # tipo_dispositivo = forms.ModelChoiceField(queryset=Tipo_Dispositivo.objects.all(), widget=ModelSelect2Widget(model=Tipo_Dispositivo,search_fields=['tipo_dispositivo'],))
    tipo_dispositivo = forms.ModelChoiceField(queryset= Prestiti_Tipo_Dispositivo.objects.all(), )
    produttore = forms.ModelChoiceField(queryset = Prestiti_Produttore.objects.all(),)
    modello = forms.ModelChoiceField(queryset = Prestiti_Modello.objects.all(),)
    # utente = forms.ModelChoiceField(queryset=Utente.objects.all(), )

    def clean_data_checkout(self):           # metodo per la validazione del campo data_checkout
        data_checkout = self.cleaned_data['data_checkout']
        if data_checkout:
            if data_checkout < self.cleaned_data['data_checkin']:
                raise forms.ValidationError(u'la data di checkout non può essere antecedente alla data di checkin')

        return data_checkout


    class Meta:
        model = Prestiti_Dispositivo
        fields = (
            'asset',
            # 'location',
            # 'palazzo',
            # 'piano',
            # 'stanza',
            'tipo_dispositivo',
            'produttore',
            'modello',
            'seriale',
            'data_checkin',
            'data_checkout',
            'fine_garanzia',
            # 'utente',
            'os',
            'note',
            'disponibile',
            # 'utenti',
        )


class Prestiti_Tipo_DispositivoForm(forms.ModelForm):

    def clean_Tipo_Dispositivo(self):  # metodo per normalizzare automaticamente l'input nella forma Xxxxxx
        return self.cleaned_data['tipo_dispositivo'].capitalize()

    class Meta:
        model = Prestiti_Tipo_Dispositivo
        fields = (
            'tipo_dispositivo',
        )

class Prestiti_ProduttoreForm(forms.ModelForm):

    def clean_produttore(self):  # metodo per normalizzare automaticamente l'input nella forma Xxxxxx
        return self.cleaned_data['produttore'].capitalize()

    class Meta:
        model = Prestiti_Produttore
        fields = (
            'produttore',
        )

class Prestiti_ModelloForm(forms.ModelForm):

    def clean_Modello(self):  # metodo per normalizzare automaticamente l'input nella forma Xxxxxx
        return self.cleaned_data['modello'].capitalize()

    class Meta:
        model = Prestiti_Modello
        fields = (
            'modello',
        )





