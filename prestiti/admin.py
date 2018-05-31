from django.contrib import admin
from django.shortcuts import render

from .models import Prestito, Prestiti_Tipo_Dispositivo, Prestiti_Produttore, Prestiti_Modello, Prestiti_Dispositivo, Prestiti_Allegato
from .forms import PrestitoCreateForm, PrestitoChangeForm, Prestiti_DispositivoForm, Prestiti_AllegatoForm
from weasyprint import HTML
from django.contrib import messages
from django.utils.safestring import mark_safe
# Register your models here.



class Prestiti_AllegatoAdmin(admin.TabularInline):
    model = Prestiti_Allegato
    form = Prestiti_AllegatoForm
    extra = 0
    # list_display = ['descrizione']
    readonly_fields = ['inserito_il']
    list_display = ['allegato', 'descrizione', 'inserito_il']


class PrestitoAdmin(admin.ModelAdmin):


    # qui si fa l'override del metodo predefinito per generare il messaggio che integra il link solo dopo l'aggiunta di un prestito
    def response_post_save_add(self, request, obj):
        messages.add_message(request, messages.WARNING, mark_safe("<bold><h1><a href=\'/crea_pdf_prestito/\'>stampa il modulo di consegna</a></h1></bold>"))
        return super(PrestitoAdmin, self).response_post_save_add(request, obj)



    # form = PrestitoChangeForm
    inlines = [Prestiti_AllegatoAdmin]
    # list_display = ['id', 'fk_dispositivo', 'fk_utente', 'tecnico_consegna', 'inizio_prestito', 'tecnico_ritiro','fine_prestito', ]
    list_display = ['id', 'fk_dispositivo', 'fk_utente', 'tecnico_consegna', 'inizio_prestito', 'tecnico_ritiro', 'fine_prestito', ]

    list_filter =  ['fk_dispositivo', 'fk_utente']
    # search_fields =  [ ]
    fields = ('fk_utente', 'fk_dispositivo',('tecnico_consegna','inizio_prestito', ),( 'tecnico_ritiro','fine_prestito',), 'note')


####### funzione per cancellare dalla lista l'action "delete_selected" ##########

    def get_actions(self, request):
        actions = super(PrestitoAdmin, self).get_actions(request)

        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

################################################################################


    def add_view(self, request, form_url='', extra_context=None):
        self.form = PrestitoCreateForm
        return super(PrestitoAdmin, self).add_view(request, )



    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.form = PrestitoChangeForm
        return super(PrestitoAdmin, self).change_view(request, object_id)



    # def save_model(self, request, obj, form, add):            # override del metodo nativo per poter salvare l'utente loggato nel campo 'tecnico'
    #     obj.tecnico_consegna = str(request.user).replace(".", " ")
    #     super(PrestitoAdmin, self).save_model(request, obj, form, add)


    class Media:
        js = (
            '/static/prestiti_tooltip.js',
            '/static/prestiti_tooltip_init.js',

            # '/static/prestiti_scelta_dispositivo.js',
            # '/static/prestiti_scelta_produttore.js',
            '/static/prestiti_popola_modello.js',
            '/static/prestiti_popola_produttore.js',

            '/static/crea_pdf_prestito.js',
        )
#
#

class Prestiti_DispositivoAdmin(admin.ModelAdmin):

    # def __init__(self):


    form = Prestiti_DispositivoForm
    # date_hierarchy = 'data_installazione'
    # ordering = ['-data_installazione']



    # def get_queryset(self, request):                                       # qui si fa filtro sul campo data_dismissione
    #     qs = super(DispositivoAdmin, self).get_queryset(request)           # per capire se il dispositivo è radiato
    #     return qs.filter(data_dismissione__isnull=False)



####### funzione per cancellare dalla lista l'action "delete_selected" ##########

    def get_actions(self, request):
        actions = super(Prestiti_DispositivoAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

#################################################################################

    # list_display = ['asset', 'tipo_dispositivo', 'produttore', 'data_installazione', 'data_dismissione', 'fine_garanzia', 'utente', 'location',]
    list_display = ['asset', 'seriale', 'tipo_dispositivo', 'produttore', 'modello', 'data_checkin', 'data_checkout', 'fine_garanzia', 'disponibile',]

    list_filter = ['tipo_dispositivo', 'disponibile', ]

    ordering =  ['-disponibile', ]


    search_fields = ['asset','seriale', 'produttore__produttore', 'modello__modello', ]
    # search_fields = ['asset', 'seriale', 'produttore', 'modello', ]


    class Media:
        js = (

            '/static/dispositivi_search_hints.js',

            # '/static/popola_fk_dispositivo.js',
            '/static/popola_asset.js',
            '/static/dispositivi_tooltip.js',
            '/static/dispositivi_tooltip_init.js',
            # '/static/dispositivi_tooltip_init.js',
            # '/static/aggiungi_allegato_hints.js',
            '/static/prestiti_scelta_produttore.js',
            '/static/prestiti_popola_modello.js',
            '/static/prestiti_popola_produttore.js',


        )

class Prestiti_Tipo_DispositivoAdmin(admin.ModelAdmin):

####### funzione per cancellare dalla lista l'action "delete_selected" ##########

    def get_actions(self, request):
        actions = super(Prestiti_Tipo_DispositivoAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

################################################################################


class Prestiti_ProduttoreAdmin(admin.ModelAdmin):

####### funzione per cancellare dalla lista l'action "delete_selected" ##########

    def get_actions(self, request):
        actions = super(Prestiti_ProduttoreAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

#################################################################################


class Prestiti_ModelloAdmin(admin.ModelAdmin):

    list_display = ['modello', 'fk_tipo_dispositivo', 'fk_produttore', 'attivo',]
    list_filter = ['fk_tipo_dispositivo', 'attivo', ]
    search_fields = ['modello', 'fk_produttore__produttore']

####### funzione per cancellare dalla lista l'action "delete_selected" ##########

    def get_actions(self, request):
        actions = super(Prestiti_ModelloAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

#################################################################################

    class Media:
        js =(
            '/static/prestiti_modelli_search_hints.js',
        )










admin.site.register(Prestito, PrestitoAdmin)
admin.site.register(Prestiti_Dispositivo, Prestiti_DispositivoAdmin)
admin.site.register(Prestiti_Tipo_Dispositivo, Prestiti_Tipo_DispositivoAdmin)
admin.site.register(Prestiti_Produttore, Prestiti_ProduttoreAdmin)
admin.site.register(Prestiti_Modello, Prestiti_ModelloAdmin)
