from django.contrib import admin
from django.conf.urls import url
from .models import Utente
from dispositivi.models import Dispositivo
from .forms import UtenteForm
from django.db import connection
from django.urls import reverse
from django.utils.html import format_html


# Register your models here.

# class AssociazioneInLine(admin.TabularInline):
#     model = Associazione
    # fields = ['nome', 'cognome', 'ruolo']
# class AssociazioneAdmin(admin.ModelAdmin):
#     pass

class DispositivoAdmin(admin.TabularInline):

    model = Dispositivo
    fk_name = 'utente'

    def get_queryset(self, request):                                # qui si fa filtro sul campo data_dismissione
        qs = super(DispositivoAdmin, self).get_queryset(request)    # per capire se il dispositivo è radiato
        return qs.filter(data_dismissione__isnull=True)

    extra = 0
    can_delete = False
    show_change_link = True


    max_num = 0  # qui si rimuove l'opzione 'aggiungi un altro' dalla visualizzazione inline
    fields = ['asset', 'location', 'tipo_dispositivo', 'seriale', 'produttore', 'modello', 'data_installazione', 'fine_garanzia',]
    readonly_fields = ['asset', 'location', 'tipo_dispositivo', 'seriale', 'produttore', 'modello', 'data_installazione', 'fine_garanzia',]
    ordering = ['location', '-data_installazione', ]

    list_display = ['asset', 'location', 'tipo_dispositivo', 'seriale', 'produttore', 'modello', 'data_installazione', 'fine_garanzia',]

    # def get_formset(self, request, obj=None, **kwargs):
    #     formset = super(DispositivoAdmin, self).get_formset(request, obj, **kwargs)
    #     form = formset.form
    #     widget = form.base_fields['asset'].widget
    #     widget.can_add_related = False
    #     return formset



class UtenteAdmin(admin.ModelAdmin):

    def get_queryset(self, request):                                  # qui si fa filtro sul campo data_dismissione
        qs = super(UtenteAdmin, self).get_queryset(request)           # per capire se il dispositivo è radiato
        return qs.filter(attivo__isnull=False)


    def correlati(self, object):

        # def show_url(self, id):
        #     url = reverse("anagrafica", id)
        #     response = format_html("""<a href="{0}">{1}</a>""", url, url)
        #     return response

        cursor = connection.cursor()
        correlati = []
        x = object.id
        cursor.execute(
            '''SELECT DISTINCT anagrafica_utente.nome, anagrafica_utente.cognome, anagrafica_utente.id
            FROM anagrafica_utente
            JOIN anagrafica_utente_segretaria_associata 
            ON anagrafica_utente_segretaria_associata.from_utente_id = anagrafica_utente.id
            WHERE anagrafica_utente_segretaria_associata.to_utente_id = %s
            ORDER BY anagrafica_utente.cognome''' %(x)
        )
        rows = cursor.fetchall()
        lista = []
        for persona in rows:
            lista.append(str(persona[0]) + " " + persona[1] + " ")

        return  " ".join(lista)



## funzione per cancellare dalla lista l'action "delete_selected" ##########

    def get_actions(self, request):
        actions = super(UtenteAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

##############################################################################

    list_display = ['matricola', 'nome', 'cognome', 'divisione', 'attivo', 'ruolo', 'correlati']

    form = UtenteForm
    actions = None
    search_fields = ['matricola', 'nome', 'cognome', 'ruolo' ]
    list_filter = ['attivo', 'divisione', 'ruolo']
    # list_display_links = ['matricola', 'correlati']
    # list_filter = ['ruolo', 'attivo']
    inlines = [DispositivoAdmin]

    class Media:
        js = (
            '/static/anagrafica_search_hints.js',
        )


admin.site.register(Utente, UtenteAdmin)

# admin.site.register(Associazione, AssociazioneAdmin)

admin.site_url = None
# admin.site.site_header = ('Gestione Supporto Enhanced')
# admin.site.site_title = ('Gestione Supporto Enhanced')
# admin.site.index_title = ('Gestione Supporto Enhanced')
