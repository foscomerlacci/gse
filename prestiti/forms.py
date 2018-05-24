from django import forms
from django.contrib.auth.models import User
from django.http import request
# from django_select2.forms import ModelSelect2Widget, Select2Widget
from django.http import HttpRequest
from django.db import connection
from django.db.models import signals
from django.http import request
from .fields import RestrictedFileField
from django.conf import settings


from .models import Prestito, Prestiti_Tipo_Dispositivo, Prestiti_Produttore, Prestiti_Modello, Prestiti_Dispositivo, Prestiti_Allegato


class PrestitoCreateForm(forms.ModelForm):

    fk_dispositivo = forms.ModelChoiceField(queryset= Prestiti_Dispositivo.objects.filter(disponibile="1").filter(data_checkout__isnull=True), label= "Dispositivo")
    tecnico_consegna = forms.ModelChoiceField(queryset=User.objects.all())
    note = forms.CharField(max_length=500, widget=forms.Textarea, required=False)


    class Media:
        js = (
            # '/static/popola_fk_dispositivo.js',
            # '/static/popola_asset.js',
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

    # fk_dispositivo = forms.ModelChoiceField(queryset= Prestiti_Dispositivo.objects.filter(disponibile="1"), label= "Dispositivo")
    # fk_dispositivo = forms.ModelChoiceField(queryset=Prestiti_Dispositivo.objects.all(),label="Dispositivo")
    # fk_utente = forms.CharField()
        note = forms.CharField(max_length=500, widget=forms.Textarea, required=False)


    class Media:
        js = (
            # '/static/popola_fk_dispositivo.js',
            # '/static/popola_asset.js',

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





