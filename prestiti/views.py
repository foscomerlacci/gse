# -*- coding: utf-8 -*-


from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import json
from dispositivi.models import Produttore
from django.db import connection
from .models import Prestito
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML, CSS
import tempfile
from datetime import datetime







def get_Produttore(request):
    id = request.GET.get('id','')
    result = list(Produttore.objects.filter(id=int(id)).select_related().values('id','produttore'))
    return HttpResponse(json.dumps(result), content_type="application/json")





def get_Modello(request):
    id_tipo_dispositivo = request.GET.get('id_tipo_dispositivo', '')
    id_produttore = request.GET.get('id_produttore', '')
    cursor = connection.cursor()
    cursor.execute('''SELECT DISTINCT prestiti_prestiti__modello.id, prestiti_prestiti_modello.modello
                      FROM prestiti_prestiti_produttore
                      JOIN prestiti_prestiti_modello
                      ON prestiti_prestiti_modello.fk_produttore_id = prestiti_prestiti_produttore.id
                      WHERE prestiti_prestiti_modello.fk_tipo_dispositivo_id = %s AND prestiti_prestiti_modello.attivo = 1 AND prestiti_prestiti_produttore.id = %s''' % (id_tipo_dispositivo, id_produttore))

    rows = cursor.fetchall()

    rowarray_list = []                  # qui si converte la tupla di tuple restituita dal cursor.execute
    for row in rows:                    # in lista
        t = (row[0], row[1])
        rowarray_list.append(t)

    return HttpResponse(json.dumps(rowarray_list), content_type="application/json")





def get_Disponibili(request):
    cursor = connection.cursor()
    cursor.execute('''SELECT prestiti_prestiti_dispositivo.id, prestiti_prestiti_dispositivo.asset
                      FROM prestiti_prestiti_dispositivo
                      WHERE prestiti_prestiti_dispositivo.disponibile = 1 ''')

    rows = cursor.fetchall()

    rowarray_list = []                  # qui si converte la tupla di tuple restituita dal cursor.execute
    for row in rows:                    # in lista
        t = (row[0], row[1])
        rowarray_list.append(t)

    return HttpResponse(json.dumps(rowarray_list), content_type="application/json")




def crea_pdf_prestito(request, ):

    prestito = Prestito.objects.raw('SELECT * FROM prestiti_prestito ORDER BY id DESC LIMIT 1') # qui si recupera l'ultimo prestito da passare alla creazione del pdf
                                                                                                # dopo essere passati dal template html

    html_string = render_to_string('prestito.html', {'prestito': prestito})
    html = HTML(string = html_string, base_url= request.build_absolute_uri())
    CSS(string='@page { size: A4; margin: 1cm }')
    result = html.write_pdf()

    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'attachment; filename='+ datetime.now().strftime("%Y-%m-%d@%H%M") +'.pdf'
    # response['Content-Disposition'] = 'attachment; filename=lista_prestiti.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())

    return response
