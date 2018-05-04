from django import forms
from .models import Utente
from nameparser import HumanName  # libreria per capitalizzare nomi e cognomi in modalita' smart


# def trova_segretarie():
#     return Utente.objects.filter(ruolo='seg')


class UtenteForm(forms.ModelForm):

    segretaria_associata = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple(), queryset=Utente.objects.filter(ruolo='seg'), required=False)

    def clean_nome(self):                                   # metodo per normalizzare automaticamente l'input nella forma Xxxxxx
        nome = HumanName(self.cleaned_data['nome'])
        nome.capitalize(force=True)
        return nome

    def clean_cognome(self):
        cognome = HumanName(self.cleaned_data['cognome'])
        cognome.capitalize(force=True)
        return cognome

    class Meta:
        model = Utente
        fields = (
            'nome',
            'cognome',
            'matricola',
            'utenza',
            'divisione',
            'ruolo',
            'attivo',
            'segretaria_associata',
        )

        widgets = {
            # 'attivo': forms.BooleanField()
            # 'ruolo': forms.Select(choices=Utente.scelte_ruolo),
            # 'segretaria_associata': forms.ModelMultipleChoiceField(queryset=Utente.objects.filter(ruolo='seg')),
            # 'segretaria_associata': forms.SelectMultiple(choices=lista_segretarie),
            # 'segretaria_associata' : forms.ModelMultipleChoiceField(widget=forms.SelectMultiple(),queryset=Utente.objects.filter(ruolo='seg')),

        }

    class Media:
        js = (
            '/static/nascondi_segretaria.js',
        )