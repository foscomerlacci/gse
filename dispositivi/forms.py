from django import forms
from django.http import request
# from django_select2.forms import ModelSelect2Widget, Select2Widget

from .fields import RestrictedFileField
from .models import Dispositivo, Allegato, Tipo_Dispositivo, Produttore, Modello
from anagrafica.models import Utente
from .toolbox import produttori



class DispositivoForm(forms.ModelForm):


    # def clean_tipo_dispositivo(self):                                   # metodo per normalizzare automaticamente l'input nella forma Xxxxxx
    #     return self.cleaned_data['tipo_dispositivo'].capitalize()

    # t = HttpRequest.POST.values()
    # t = HttpRequest.POST.get('bn')
    # def __init__(self, *args, **kwargs):
    #     super(DispositivoForm, self).__init__(*args, **kwargs)
    #     self.fields['produttore'].choices = list(Produttore.objects.values_list('id', 'produttore').filter())
    #     self.fields['modello'].choices = list(Modello.objects.values_list('id', 'modello'))
    # tipo_dispositivo = forms.ModelChoiceField(queryset=Tipo_Dispositivo.objects.all(), widget=ModelSelect2Widget(model=Tipo_Dispositivo,search_fields=['tipo_dispositivo'],))
    tipo_dispositivo = forms.ModelChoiceField(queryset=Tipo_Dispositivo.objects.all(), )
    produttore = forms.ModelChoiceField(queryset = Produttore.objects.all(),)
    modello = forms.ModelChoiceField(queryset = Modello.objects.all(),)




    # def clean_modello(self):  # metodo per normalizzare automaticamente l'input nella forma Xxxxxx
    #     return self.cleaned_data['modello'].capitalize()


    # tipo_dispositivo = forms.ModelChoiceField(queryset=Tipo_Dispositivo.objects.all(), widget=ModelSelect2Widget(model=Tipo_Dispositivo, search_fields=['tipo_dispositivo__icontains'],),)

    # tipo_dispositivo = forms.ModelChoiceField(queryset=Tipo_Dispositivo.objects.all(),)
    # produttore = forms.ModelChoiceField(queryset = Produttore.objects.all(), widget=ModelSelect2Widget(model=Produttore,dependent_fields={'tipo_dispositivo':'dispositivi_dispositivo.tipo_dispositivo_id'},))
    # produttore = forms.ModelChoiceField(queryset=Produttore.objects.all(), widget=ModelSelect2Widget(model=Produttore))
    # modello = forms.ModelChoiceField(queryset=Modello.objects.all(), widget=ModelSelect2Widget(model=Modello, search_fields=['modello__icontains'],  {'tipo_dispositivo': 'Dispositivo.tipo_dispositivo', }, ), )


    class Meta:
            model = Dispositivo
            fields = (
                'asset',
                'location',
                'palazzo',
                'piano',
                'stanza',
                'tipo_dispositivo',
                'produttore',
                'modello',
                'seriale',
                'data_installazione',
                'data_dismissione',
                'fine_garanzia',
                'utente',
                'note',
                # 'utenti',
                )

            widgets = {
                # 'produttore': Select2Widget,
                # 'modello': Select2Widget,
                # 'produttore':forms.Select(attrs={
                #     'id': 'tipo',
                }



    # utente = forms.CharField(label='assegnario')


class AllegatoForm(forms.ModelForm):

    class Meta:
        model = Allegato
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
                                    label= 'allegato (.doc .docx .xls .xlsx .txt .pdf .jpg  max 1 MB)')   # sovrascrivo l'etichetta del campo che fara' da intestazione



class ProduttoreForm(forms.ModelForm):

    def clean_produttore(self):  # metodo per normalizzare automaticamente l'input nella forma Xxxxxx
        return self.cleaned_data['produttore'].capitalize()

    class Meta:
        model = Produttore
        fields = (
            'produttore',
        )


class Tipo_DispositivoForm(forms.ModelForm):

    def clean_Tipo_Dispositivo(self):  # metodo per normalizzare automaticamente l'input nella forma Xxxxxx
        return self.cleaned_data['tipo_dispositivo'].capitalize()

    class Meta:
        model = Tipo_Dispositivo
        fields = (
            'tipo_dispositivo',
        )


class ModelloForm(forms.ModelForm):

    def clean_Modello(self):  # metodo per normalizzare automaticamente l'input nella forma Xxxxxx
        return self.cleaned_data['modello'].capitalize()

    class Meta:
        model = Modello
        fields = (
            'modello',
        )



