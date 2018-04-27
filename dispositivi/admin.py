from django.contrib import admin
from django.conf.urls import url
from django.shortcuts import get_object_or_404
from .forms import AllegatoForm, DispositivoForm
from .models import  Dispositivo, Allegato, Tipo_Dispositivo, Produttore, Modello
# from jet.admin import CompactInline
from django.db import connection




class AllegatoAdmin(admin.TabularInline):
    model = Allegato
    form = AllegatoForm
    extra = 0
    # list_display = ['descrizione']
    list_display = ['allegato', 'descrizione', 'datestamp']


# Register your models here.
#
# class UtenteAdmin(admin.ModelAdmin):
#     form = UtenteForm




class DispositivoAdmin(admin.ModelAdmin):

    # def __init__(self):


    form = DispositivoForm
    inlines = [AllegatoAdmin]
    date_hierarchy = 'data_installazione'
    ordering = ['-data_installazione']


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

    # list_display = ['asset', 'tipo_dispositivo', 'produttore', 'data_installazione', 'data_dismissione', 'fine_garanzia', 'utente', 'location',]
    list_display = ['asset', 'seriale', 'tipo_dispositivo', 'produttore', 'modello', 'data_installazione', 'data_dismissione', 'fine_garanzia', 'utente', 'location',]

    list_filter = ['location','tipo_dispositivo', ]


    search_fields = ['asset','seriale', 'produttore__produttore', 'modello__modello', ]
    # search_fields = ['asset', 'seriale', 'produttore', 'modello', ]


    class Media:
        js = (
            # '/static/',
            '/static/dispositivi_search_hints.js',
            '/static/popola_produttore.js',
            '/static/popola_modello.js',
            '/static/popola_asset.js',
            # '/static/aggiungi_allegato_hints.js',

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

#################################################################################

class ModelloAdmin(admin.ModelAdmin):
    model = Modello
    list_display = ['modello']

####### funzione per cancellare dalla lista l'action "delete_selected" ##########

    def get_actions(self, request):
        actions = super(ModelloAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

#################################################################################



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


