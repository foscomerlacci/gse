import json
from django.db import connection, models
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Count, Q
from interventi.models import Intervento
from django.db.models import Func, F, Count




# Create your views here.


def get_Asset(request):
    id = request.GET.get('id','')
    cursor = connection.cursor()
    # cursor.execute('''SELECT dispositivi_dispositivo.id, dispositivi_dispositivo.asset, dispositivi_modello.modello
    #                   FROM dispositivi_dispositivo
    #                   JOIN anagrafica_utente, dispositivi_modello
    #                   ON anagrafica_utente.id = dispositivi_dispositivo.utente_id AND dispositivi_dispositivo.modello_id = dispositivi_modello.id
    #                   WHERE anagrafica_utente.id = %s ''' % id)

    cursor.execute('''SELECT dispositivi_dispositivo.id, dispositivi_dispositivo.asset, dispositivi_modello.modello, dispositivi_dispositivo.location
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


def stats(request):
    return render(request, 'stats.html')


def stats_data(request):

    cursor = connection.cursor()

    cursor.execute('''select count (*), strftime("%Y-%m", data_chiusura) from interventi_intervento group by strftime("%Y-%m", data_chiusura);''')

    rows = cursor.fetchall()

    dataset = []                  # qui si converte la tupla di tuple restituita dal cursor.execute
    for row in rows:                    # in lista di int
        t = int(row[0])
        dataset.append(t)

    categories = []                  # qui si converte la tupla di tuple restituita dal cursor.execute
    for row in rows:                    # in lista di str
        t = row[1]
        categories.append(t)

    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'Tickettometro'},
        'xAxis': {'categories': categories},

        'series': [{
            # 'name': 'anno 1800',
            # 'data': [107, 31, 635, 203, 2]},{
            # 'name': 'anno 1900',
            # 'data': [133, 156, 947, 408, 6]}, {
            'name': 'totale tickets',
            'data': dataset,
            'color': 'green',
                },
            ]}


    return JsonResponse(chart)