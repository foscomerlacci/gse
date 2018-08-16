from django import forms
from .models import Contatto
from nameparser import HumanName  # libreria per capitalizzare nomi e cognomi in modalita' smart
from nameparser.config import CONSTANTS

# def trova_segretarie():
#     return Utente.objects.filter(ruolo='seg')

CONSTANTS.prefixes.remove('de','di')  # tolgo i prefissi dalla lista dei forzati minuscoli per ottenere la capitalization corretta

class ContattoForm(forms.ModelForm):

    def clean_nome(self):                                   # metodo per normalizzare automaticamente l'input nella forma Xxxxxx
        nome = HumanName(self.cleaned_data['nome'])
        nome.capitalize(force=True)
        return nome

    def clean_cognome(self):
        cognome = HumanName(self.cleaned_data['cognome'])
        cognome.capitalize(force=True)
        return cognome

    class Meta:
        model = Contatto
        fields = (
                'servizio',
                'nome',
                'cognome',
                'telefono',
                'email',
                'note',
        )