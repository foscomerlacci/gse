from django.contrib import admin
from .models import Contatto

# Register your models here.

class ContattoAdmin(admin.ModelAdmin):
    model = Contatto
    # form = ContattoForm

    search_fields = ['cognome', 'servizio',]

    list_display = ['servizio',
                    # 'area',
                    'nome',
                    'cognome',
                    'telefono',
                    'email',
                    ]

    exclude = ('area',)

    class Media:
        js = (

            '/static/contatti_search_hints.js',

        )


####### funzione per cancellare dalla lista l'action "delete_selected" ##########

    def get_actions(self, request):
        actions = super(ContattoAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

#################################################################################



admin.site.register(Contatto, ContattoAdmin)
