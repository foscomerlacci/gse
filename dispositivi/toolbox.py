import xlwt

from django.db import connection
from django.http import HttpResponse
from xlwt.compat import xrange
import sys
from PIL import Image, ExifTags


def produttori(request):
    cursor = connection.cursor()
    cursor.execute('''SELECT DISTINCT dispositivi_produttore.id, produttore 
                      FROM dispositivi_produttore JOIN dispositivi_modello
                      ON dispositivi_modello.fk_produttore_id = dispositivi_produttore.id
                      WHERE dispositivi_modello.fk_tipo_dispositivo_id = 7''')
    elencoproduttori = []
    rows = cursor.fetchall()

    for index in range(len(rows)):
        elencoproduttori.append(rows[index])
    return elencoproduttori


def modelli(request):
    cursor = connection.cursor()
    cursor.execute('''SELECT noleggi_auto.id, targa FROM noleggi_auto
                        EXCEPT
                        SELECT  noleggi_auto.id, targa FROM noleggi_auto LEFT JOIN noleggi_noleggio
                        ON (noleggi_auto.id = noleggi_noleggio.fkauto_id)
                        WHERE datauscita IS NOT NULL AND dataentrata IS NULL
                        ORDER BY targa''')
    elencomodelli = []
    rows = cursor.fetchall()

    for index in range(len(rows)):
        elencomodelli.append(rows[index])
    return elencomodelli


def export_tracciato_xls(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=ListaAsset.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("ListaAsset")

    row_num = 0

    columns = [
        (u"asset", 7000),
        (u"seriale", 7000),
        (u"tipo dispositivo", 7000),
        (u"produttore", 7000),
        (u"modello", 7000),
        (u"data installazione", 7000),
        (u"data dismissione", 7000),
        (u"fine garanzia", 7000),
        (u"assegnatario", 7000),
        (u"location", 7000),
        (u"palazzo", 7000),
        (u"piano", 7000),
        (u"stanza", 7000),
    ]

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for col_num in xrange(len(columns)):
        ws.write(row_num, col_num, columns[col_num][0], font_style)
        # set column width
        ws.col(col_num).width = columns[col_num][1]

    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1

    for objects in queryset:
        row_num += 1

        if (objects.data_installazione):
            dataInstallazione = objects.data_installazione.strftime('%d-%m-%Y')
        else:
            dataInstallazione = ""

        if (objects.data_dismissione):
            dataDismissione = objects.data_dismissione.strftime('%d-%m-%Y')
        else:
            dataDismissione = ""

        if (objects.fine_garanzia):
            fineGaranzia = objects.fine_garanzia.strftime('%d-%m-%Y')
        else:
            fineGaranzia = ""

        row = [
            objects.asset,
            objects.seriale,
            objects.tipo_dispositivo.tipo_dispositivo,
            objects.produttore.produttore,
            objects.modello.modello,
            dataInstallazione,
            dataDismissione,
            fineGaranzia,
            objects.utente.__str__(),
            objects.location,
            objects.palazzo,
            objects.piano,
            objects.stanza,
            # 'asset', 'seriale', 'tipo_dispositivo', 'produttore', 'modello', 'data_installazione', 'data_dismissione',
            # 'fine_garanzia', 'utente', 'location'
        ]
        for col_num in xrange(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response





export_tracciato_xls.short_description = u"Export XLS"
