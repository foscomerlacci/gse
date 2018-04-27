import json
from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def get_Asset(request):
    id = request.GET.get('id','')
    cursor = connection.cursor()
    # cursor.execute('''SELECT dispositivi_dispositivo.id, dispositivi_dispositivo.asset, dispositivi_modello.modello
    #                   FROM dispositivi_dispositivo
    #                   JOIN anagrafica_utente, dispositivi_modello
    #                   ON anagrafica_utente.id = dispositivi_dispositivo.utente_id AND dispositivi_dispositivo.modello_id = dispositivi_modello.id
    #                   WHERE anagrafica_utente.id = %s ''' % id)

    cursor.execute('''SELECT dispositivi_dispositivo.id, dispositivi_dispositivo.asset, dispositivi_modello.modello
                      FROM dispositivi_dispositivo
                      JOIN anagrafica_utente, dispositivi_modello
                      ON anagrafica_utente.id = dispositivi_dispositivo.utente_id AND dispositivi_dispositivo.modello_id = dispositivi_modello.id
                      WHERE anagrafica_utente.id = '%s' AND dispositivi_dispositivo.data_dismissione IS NULL''' % id)

    rows = cursor.fetchall()

    rowarray_list = []                  # qui si converte la tupla di tuple restituita dal cursor.execute
    for row in rows:                    # in lista
        t = (row[0], row[1], row[2])
        rowarray_list.append(t)

    return HttpResponse(json.dumps(rowarray_list), content_type="application/json")