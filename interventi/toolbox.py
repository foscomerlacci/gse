from django.http import HttpResponse
from xlwt.compat import xrange
import xlwt
# from .admin import InterventoAdmin

###  funzione per l'export in xls

def export_xls(modeladmin, request, queryset):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=ListaInterventi.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("ListaInterventi")

    row_num = 0

    columns = [
        (u"tecnico", 7000),
        (u"tipo servizio", 7000),
        (u"OpCo", 7000),
        (u"location", 7000),
        # (u"palazzo", 7000),
        (u"richiedente", 7000),
        (u"data richiesta", 7000),
        (u"data chiusura", 7000),
        (u"ora intervento", 7000),
        (u"cognome", 7000),
        (u"nome", 7000),
        (u"tipo asset", 7000),
        (u"asset", 7000),
        (u"tipo ticket", 7000),
        (u"numero ticket", 7000),
        (u"area intervento", 7000),
        (u"descrizione richiesta", 7000),
        (u"soluzione adottata", 7000),
        (u"stato intervento", 7000),
        (u"tipo ingaggio", 7000),
        (u"note", 7000),
    ]

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for col_num in xrange(len(columns)):
        ws.write(row_num, col_num, columns[col_num][0], font_style)
        # set column width
        ws.col(col_num).width = columns[col_num][1]

    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1

    for objects in reversed(queryset):
        row_num += 1

        # qui intercetto gli eventuali campi NULL dovuti alla non scelta del dispositivo

        if (objects.asset != None):
            location = objects.asset.location
            palazzo = objects.asset.palazzo
            tipo_dispositivo = objects.asset.tipo_dispositivo.tipo_dispositivo
            asset = objects.asset.asset
        else:
            location = ""
            palazzo = ""
            tipo_dispositivo = "Altro"
            asset = ""

        if (objects.datetime_ingaggio != None):
            datetime_ingaggio = objects.datetime_ingaggio.strftime('%d-%m-%Y %H:%M:%S')
        else:
            datetime_ingaggio = ""

        row = [
            objects.tecnico,
            objects.tipo_servizio,
            objects.fk_beneficiario.divisione,
            location,
            # palazzo,
            objects.richiedente,
            objects.data_richiesta.strftime('%d-%m-%Y'),
            objects.data_chiusura.strftime('%d-%m-%Y'),
            datetime_ingaggio,
            objects.fk_beneficiario.cognome,
            objects.fk_beneficiario.nome,
            tipo_dispositivo,
            asset,
            objects.tipo_ticket,
            objects.numero_ticket,
            objects.area_intervento,
            objects.descrizione_richiesta,
            objects.soluzione_adottata,
            objects.stato_intervento,
            objects.tipo_ingaggio,
            objects.note,

        ]
        for col_num in xrange(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


export_xls.short_description = u"Export XLS"


