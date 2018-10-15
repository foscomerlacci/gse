from django.contrib import admin
from .models import Intervento
from .forms import InterventoForm
from .toolbox import export_xls
# Register your models here.



class InterventoAdmin(admin.ModelAdmin):
    model = Intervento
    form = InterventoForm
    date_hierarchy = 'data_chiusura'

    search_fields = ['asset__asset', 'fk_beneficiario__cognome', 'fk_beneficiario__nome']

    list_display = [
                    'id',
                    'tecnico',
                    # 'richiedente',
                    'fk_beneficiario',
                    'asset',
                    'data_richiesta',
                    'tipo_ticket',
                    # 'numero_ticket',
                    'area_intervento',
                    # 'descrizione_richiesta',
                    # 'soluzione_adottata',
                    'stato_intervento',
                    # 'data_chiusura',
                    # 'tipo_ingaggio',
                    # 'note',
                    ]

    exclude = ('tecnico', 'tipo_servizio',)

    ordering = ['-data_richiesta',]

    actions = [export_xls]


####### funzione per cancellare dalla lista l'action "delete_selected" ##########

    def get_actions(self, request):
        actions = super(InterventoAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

#################################################################################

    class Media:
        js = (
            # '/static/',
            '/static/interventi_search_hints.js',
            # '/static/prestiti_popola_produttore.js',
            '/static/popola_asset.js',
            '/static/cambia_beneficiario.js',
            # '/static/aggiungi_allegato_hints.js',

        )



    def save_model(self, request, obj, form, add):            # override del metodo nativo per poter salvare l'utente loggato nel campo 'tecnico' SOLO IN FASE DI CREAZIONE INTERVENTO
        if obj.tecnico == None:
            obj.tecnico = str(request.user).replace(".", " ")
            super(InterventoAdmin, self).save_model(request, obj, form, add)
        else:
            super(InterventoAdmin, self).save_model(request, obj, form, add)




admin.site.register(Intervento, InterventoAdmin)
