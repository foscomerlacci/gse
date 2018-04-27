from django.db  import connection
from django.http import HttpResponse
import sys


def produttori(request):
    cursor = connection.cursor()
    cursor.execute('''select distinct dispositivi_produttore.id, produttore 
                      from dispositivi_produttore join dispositivi_modello
                      on dispositivi_modello.fk_produttore_id = dispositivi_produttore.id
                      where dispositivi_modello.fk_tipo_dispositivo_id = 7''')
    elencoproduttori = []
    rows = cursor.fetchall()

    for index in range(len(rows)):
        elencoproduttori.append(rows[index])
    return elencoproduttori



def modelli(request):
    cursor = connection.cursor()
    cursor.execute('''select noleggi_auto.id, targa from noleggi_auto
                        except
                        select  noleggi_auto.id, targa from noleggi_auto left join noleggi_noleggio
                        on (noleggi_auto.id = noleggi_noleggio.fkauto_id)
                        where datauscita is not null and dataentrata is null
                        ORDER BY targa''')
    elencomodelli = []
    rows = cursor.fetchall()

    for index in range(len(rows)):
        elencomodelli.append(rows[index])
    return elencomodelli