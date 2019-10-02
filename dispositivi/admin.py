from django.contrib import admin
from django.conf.urls import url
from django.shortcuts import get_object_or_404

from dispositivi.toolbox import export_tracciato_xls
from dispositivi.forms import AllegatoForm, DispositivoForm
from dispositivi.models import Dispositivo, Allegato, Tipo_Dispositivo, Produttore, Modello
from anagrafica.models import Utente
# from jet.admin import CompactInline
from django.db import connection
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import SimpleListFilter


## qui creo il filtro personalizzato per mostrare di default solo i dispositivi in uso a utenti attivi ################

class FiltroUtenteAttivo(SimpleListFilter):
    title = _('utente')
    parameter_name = 'utente__attivo'

    def lookups(self, request, model_admin):
        return (
            (None, _('attivo')),
            ('False', _('non attivo')),
            ('tutti', _('tutti')),
        )

    def choices(self, cl):
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == lookup,
                'query_string': cl.get_query_string({
                    self.parameter_name: lookup,
                }, []),
                'display': title,
            }

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset.filter(utente__attivo=True)
        if self.value() == 'False':
            return queryset.filter(utente__attivo=False)


#######################################################################################################################




class AllegatoAdmin(admin.TabularInline):
    model = Allegato
    form = AllegatoForm
    extra = 0
    # list_display = ['descrizione']
    readonly_fields = ['inserito_il']
    list_display = ['allegato', 'descrizione', 'inserito_il']


# Register your models here.
#
# class UtenteAdmin(admin.ModelAdmin):
#     form = UtenteForm




class DispositivoAdmin(admin.ModelAdmin):
    # def __init__(self):


    form = DispositivoForm
    inlines = [AllegatoAdmin]
    date_hierarchy = 'data_installazione'
    ordering = ['location', '-data_installazione']
    actions = [export_tracciato_xls]

    autocomplete_fields = ['utente']

    # qui si trova lo stato attivo/non attivo dell'assegnatario ####################

    # def attivo(self, object):
    #     cursor = connection.cursor()
    #     x = object.id
    #     cursor.execute(
    #         '''SELECT DISTINCT   anagrafica_utente.attivo
    #             FROM anagrafica_utente
    #             JOIN dispositivi_dispositivo
    #             ON  dispositivi_dispositivo.utente_id = anagrafica_utente.id
    #             WHERE dispositivi_dispositivo.id = %s''' %(x)
    #     )
    #     rows = cursor.fetchone()
    #     return  rows

    #################################################################################




    # def get_queryset(self, request):                                       # qui si fa filtro sul campo data_dismissione
    #     qs = super(DispositivoAdmin, self).get_queryset(request)           # per capire se il dispositivo è radiato
    #     return qs.filter(data_dismissione__isnull=False)



    ####### funzione per cancellare dalla lista l'action "delete_selected" ##########

    def get_actions(self, request):
        actions = super(DispositivoAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    #################################################################################

    # list_display = ['asset', 'tipo_dispositivo', 'produttore', 'data_installazione', 'data_dismissione', 'fine_garanzia', 'attivo', 'location',]
    list_display = ['asset', 'seriale', 'tipo_dispositivo', 'produttore', 'modello', 'data_installazione',
                    'data_dismissione', 'fine_garanzia', 'utente', 'location', ]

    list_filter = [FiltroUtenteAttivo, 'location', 'tipo_dispositivo', ]

    search_fields = ['asset', 'seriale', 'produttore__produttore', 'modello__modello', 'utente__nome',
                     'utente__cognome', ]

    # search_fields = ['asset', 'seriale', 'produttore', 'modello', ]


    class Media:
        js = (

            '/static/dispositivi_search_hints.js',
            '/static/dispositivi_tooltip.js',
            '/static/dispositivi_tooltip_init.js',
            # # '/static/popola_fk_dispositivo.js',
            # # '/static/dispositivi_tooltip_init.js',
            # # '/static/aggiungi_allegato_hints.js',
            # # '/static/popola_asset.js',
            # '/static/scelta_dispositivo.js',
            # '/static/scelta_produttore.js',
            '/static/popola_modello.js',
            '/static/popola_produttore.js',
            '/static/cambia_location.js',
            '/static/cambia_modello.js',
            '/static/double_click_prevent_input.default.js',
            '/static/double_click_prevent_input_continue.js',
            '/static/double_click_prevent_input_addanother.js',
            '/static/js/notifIt.js',

        )


class TipoDispositivoAdmin(admin.ModelAdmin):
    model = Tipo_Dispositivo
    list_display = ['tipo_dispositivo']

    ####### funzione per cancellare dalla lista l'action "delete_selected" ##########

    def get_actions(self, request):
        actions = super(TipoDispositivoAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    class Media:
        js = (

            '/static/double_click_prevent_input.default.js',
            '/static/double_click_prevent_input_continue.js',
            '/static/double_click_prevent_input_addanother.js',
            '/static/js/notifIt.js',
        )

        #################################################################################


class ProduttoreAdmin(admin.ModelAdmin):
    model = Produttore
    list_display = ['produttore']

    ####### funzione per cancellare dalla lista l'action "delete_selected" ##########

    def get_actions(self, request):
        actions = super(ProduttoreAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    class Media:
        js = (

            '/static/double_click_prevent_input.default.js',
            '/static/double_click_prevent_input_continue.js',
            '/static/double_click_prevent_input_addanother.js',
            '/static/js/notifIt.js',
        )


#################################################################################

class ModelloAdmin(admin.ModelAdmin):
    model = Modello
    list_display = ['modello', 'fk_tipo_dispositivo', 'fk_produttore', 'attivo', ]
    list_filter = ['fk_tipo_dispositivo', 'attivo', ]
    search_fields = ['modello', 'fk_produttore__produttore']

    ####### funzione per cancellare dalla lista l'action "delete_selected" ##########

    def get_actions(self, request):
        actions = super(ModelloAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    #################################################################################

    class Media:
        js = (
            '/static/modelli_search_hints.js',
            '/static/double_click_prevent_input.default.js',
            '/static/double_click_prevent_input_continue.js',
            '/static/double_click_prevent_input_addanother.js',
            '/static/js/notifIt.js',
        )


# @admin.register(Dispositivo)
# class DispositivoAdmin(admin.ModelAdmin):



# admin.site.register(Utente, UtenteAdmin)
admin.site.register(Dispositivo, DispositivoAdmin)
admin.site.register(Tipo_Dispositivo, TipoDispositivoAdmin)
admin.site.register(Produttore, ProduttoreAdmin)
admin.site.register(Modello, ModelloAdmin)

admin.site_url = None
# admin.site.site_header = ('Gestione Supporto Enhanced')
# admin.site.site_title = ('Gestione Supporto Enhanced')
# admin.site.index_title = ('Gestione Supporto Enhanced')
