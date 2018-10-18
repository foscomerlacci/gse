from django import forms
from django.http import request
# from django_select2.forms import ModelSelect2Widget, Select2Widget


from .models import Intervento





class InterventoForm(forms.ModelForm):
    # pass

    # tecnico = forms.HiddenInput()

    def clean_data_chiusura(self):           # metodo per la validazione del campo data_chiusura
        data_chiusura = self.cleaned_data['data_chiusura']

        if self.cleaned_data.get('data_richiesta') is not None:   # qui si intercetta la possibile data_richiesta con valore nullo
            data_richiesta = self.cleaned_data['data_richiesta']
            if data_chiusura < data_richiesta:
                raise forms.ValidationError(u'la data di chiusura intervento non può essere antecedente a quella di richiesta')

        return data_chiusura


    class Media:
        js = (
            # '/static/',
            '/static/popola_asset.js',
            '/static/nascondi_datetime_ingaggio.js',

        )


    class Meta:
        model = Intervento

        fields = (

            'richiedente',
            'data_richiesta',
            'fk_beneficiario',
            'asset',
            'tipo_ticket',
            'numero_ticket',
            'area_intervento',
            'descrizione_richiesta',
            'data_chiusura',
            'tipo_ingaggio',
            'datetime_ingaggio',
            'stato_intervento',
            'soluzione_adottata',

            'note',

            )

        widgets = {
            # 'tecnico': forms.HiddenInput()
        }
