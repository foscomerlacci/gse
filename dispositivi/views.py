from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import json
from dispositivi.models import Produttore
from django.db import connection

#
# def get_Produttore(request):
#     id = request.GET.get('id','')
#     result = list(Produttore.objects.filter(id=int(id)).select_related().values('id','produttore'))
#     return HttpResponse(json.dumps(result), content_type="application/json")




def get_Produttore(request):
    id = request.GET.get('id','')
    cursor = connection.cursor()
    cursor.execute('''SELECT DISTINCT dispositivi_produttore.id , dispositivi_produttore.produttore \
                      FROM dispositivi_produttore JOIN dispositivi_modello\
                      ON dispositivi_modello.fk_produttore_id = dispositivi_produttore.id\
                      WHERE dispositivi_modello.fk_tipo_dispositivo_id = %s ''' % id)

    rows = cursor.fetchall()

    rowarray_list = []                  # qui si converte la tupla di tuple restituita dal cursor.execute
    for row in rows:                    # in lista
        t = (row[0], row[1])
        rowarray_list.append(t)

    return HttpResponse(json.dumps(rowarray_list), content_type="application/json")




def get_Modello(request):
    id_tipo_dispositivo = request.GET.get('id_tipo_dispositivo', '')
    id_produttore = request.GET.get('id_produttore', '')
    cursor = connection.cursor()
    cursor.execute('''SELECT DISTINCT dispositivi_modello.id, dispositivi_modello.modello
                      FROM dispositivi_produttore 
                      JOIN dispositivi_modello
                      ON dispositivi_modello.fk_produttore_id = dispositivi_produttore.id
                      WHERE dispositivi_modello.fk_tipo_dispositivo_id = %s AND dispositivi_modello.attivo = 1 AND dispositivi_produttore.id = %s''' % (id_tipo_dispositivo, id_produttore))

    rows = cursor.fetchall()

    rowarray_list = []                  # qui si converte la tupla di tuple restituita dal cursor.execute
    for row in rows:                    # in lista
        t = (row[0], row[1])
        rowarray_list.append(t)

    return HttpResponse(json.dumps(rowarray_list), content_type="application/json")
