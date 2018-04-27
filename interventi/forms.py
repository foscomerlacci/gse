from django import forms
from django.http import request
# from django_select2.forms import ModelSelect2Widget, Select2Widget


from .models import Intervento





class InterventoForm(forms.ModelForm):
    # pass

    # tecnico = forms.HiddenInput()



    class Media:
        js = (
            # '/static/',
            '/static/popola_asset.js',

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
            'stato_intervento',
            'soluzione_adottata',

            'note',

            )

        widgets = {
            # 'tecnico': forms.HiddenInput()
        }
