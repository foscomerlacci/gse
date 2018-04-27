from django import forms
from .models import Utente


# def trova_segretarie():
#     return Utente.objects.filter(ruolo='seg')


class UtenteForm(forms.ModelForm):

    segretaria_associata = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple(), queryset=Utente.objects.filter(ruolo='seg'), required=False)

    def clean_nome(self):                                   # metodo per normalizzare automaticamente l'input nella forma Xxxxxx
        return self.cleaned_data['nome'].capitalize()

    def clean_cognome(self):
        return self.cleaned_data['cognome'].capitalize()

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