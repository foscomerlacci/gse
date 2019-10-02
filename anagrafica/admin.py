from django.contrib import admin
from django.conf.urls import url
from .models import Utente
from dispositivi.models import Dispositivo
from .forms import UtenteForm
from django.db import connection
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import SimpleListFilter


# Register your models here.

# class AssociazioneInLine(admin.TabularInline):
#     model = Associazione
    # fields = ['nome', 'cognome', 'ruolo']
# class AssociazioneAdmin(admin.ModelAdmin):
#     pass







## qui creo il filtro personalizzato per mostrare di default solo i dispositivi in uso a utenti attivi ################

class FiltroUtenteAttivo(SimpleListFilter):
    title = _('utente')
    parameter_name = 'attivo'

    def lookups(self, request, model_admin):
        return(
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
            return queryset.filter(attivo=True)
        if self.value() == 'False':
            return  queryset.filter(attivo=False)

#######################################################################################################################


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
    class Media:
        js = (
            '/static/double_click_prevent_input.default.js',
            '/static/double_click_prevent_input_continue.js',
            '/static/double_click_prevent_input_addanother.js',
            '/static/js/notifIt.js',
            # '/static/aggiungi_allegato_hints.js',

        )


class UtenteAdmin(admin.ModelAdmin):

    # def get_queryset(self, request):                                  # qui si fa filtro sul campo attivo
    #     qs = super(UtenteAdmin, self).get_queryset(request)           # per capire se l'utente è attivo
    #     return qs.filter(attivo__isnull=False)






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
            lista.append(str(persona[0]) + " " + persona[1] + ", ")

        return  str(" ".join(lista))[:-2]

################################################################################################################

    def lista_segretarie(self, object):
        # def show_url(self, id):
        #     url = reverse("anagrafica", id)
        #     response = format_html("""<a href="{0}">{1}</a>""", url, url)
        #     return response

        cursor = connection.cursor()
        cursor.execute(
            '''SELECT DISTINCT anagrafica_utente.nome, anagrafica_utente.cognome, anagrafica_utente.id
            FROM anagrafica_utente        
            WHERE anagrafica_utente.ruolo = 'seg' AND anagrafica_utente.attivo = 1
            ORDER BY anagrafica_utente.cognome'''
        )
        rows = cursor.fetchall()
        lista = []
        for persona in rows:
            lista.append(str(persona[0]) + " " + persona[1] + " , ")

        return " ".join(lista)

################################################################################################################

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
    list_filter = [FiltroUtenteAttivo, 'divisione', 'ruolo']
    ordering = ['cognome',]
    # list_display_links = ['matricola', 'correlati']
    # list_filter = ['ruolo', 'attivo']
    inlines = [DispositivoAdmin]

    class Media:
        js = (
            '/static/anagrafica_search_hints.js',
            '/static/double_click_prevent_input.default.js',
            '/static/double_click_prevent_input_continue.js',
            '/static/double_click_prevent_input_addanother.js',
            '/static/js/notifIt.js',
        )


admin.site.register(Utente, UtenteAdmin)

# admin.site.register(Associazione, AssociazioneAdmin)

admin.site_url = None
# admin.site.site_header = ('Gestione Supporto Enhanced')
# admin.site.site_title = ('Gestione Supporto Enhanced')
# admin.site.index_title = ('Gestione Supporto Enhanced')
