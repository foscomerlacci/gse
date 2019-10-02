#! /usr/bin/python3

import random
import string
from faker import Faker
from datetime import datetime
import sqlite3

fake = Faker()


scelte_tipo_ticket = ('incident',
                      'IMAC',
                      'change',
                      'move',
                      'altro',)

scelte_stato_intervento = ('chiuso',
                           'work in progress',
                           'pianificato',
                           'counter stop',
                           'cancellato',)

scelte_tipo_ingaggio = ('mail enhanced',
                        'mail Coppetta',
                        'telefonata enhanced',
                        'telefonata Coppetta',
                        'telefonata utente',)

scelte_area_intervento = ('Applicativi',
                          'Aree condivise',
                          'Backup/ripristino',
                          'Informazioni/procedure',
                          'Messaging',
                          'Mobile',
                          'Move',
                          'PC HW',
                          'PC SW',
                          'Printing',
                          'Sicurezza',
                          'TLC',
                          'User Management',
                          'Video/Audio comunicazione',
                          'altro',)

lista_dispositivi = []
lista_tecnici = []
lista_interventi = []

sql_intervento = """INSERT INTO interventi_intervento (tecnico, 
                                            tipo_servizio, 
                                            richiedente, 
                                            data_richiesta, 
                                            tipo_ticket, 
                                            area_intervento, 
                                            descrizione_richiesta, 
                                            soluzione_adottata, 
                                            stato_intervento,
                                            asset_id,
                                            fk_beneficiario_id,
                                            data_chiusura,
                                            tipo_ingaggio) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"""



db = sqlite3.connect('../../gse.sqlite3')
cur = db.cursor()
cur.execute("""SELECT id, utente_id, data_installazione FROM dispositivi_dispositivo""")  # qui estrae tutti i dispositivi e ottengo "lista_dispositivi"
for row in cur:
    dispositivo = [row[0], row[1], datetime.strptime(row[2], '%Y-%m-%d'),]
    # print(type(row[2]))
    lista_dispositivi.append(dispositivo)
db.close()

# print(lista_dispositivi)


db = sqlite3.connect('../../gse.sqlite3')
cur = db.cursor()
cur.execute("""SELECT first_name, last_name FROM auth_user WHERE first_name != 'root'""")  # qui estrae tutti i tecnici
for row in cur:
    tecnico = str(row[0] + " " + row[1])
    lista_tecnici.append(tecnico)
db.close()

# print(lista_tecnici)

for d in lista_dispositivi:
    tecnico = random.choice(lista_tecnici)
    tipo_servizio = "enhanced"
    richiedente = "Richie Dente"
    data_richiesta = fake.date_between(start_date=d[2], end_date='today')
    tipo_ticket = random.choice(scelte_tipo_ticket)
    area_intervento = random.choice(scelte_area_intervento)
    descrizione_richiesta = "richiesta richiesta richiesta richiesta richiesta richiesta richiesta richiesta richiesta richiesta richiesta richiesta"
    soluzione_adottata = "soluzione soluzione soluzione soluzione soluzione soluzione soluzione soluzione soluzione soluzione soluzione soluzione"
    stato_intervento = random.choice(scelte_stato_intervento)
    asset_id = d[0]
    fk_beneficiario_id = d[1]
    data_chiusura = data_richiesta
    tipo_ingaggio = random.choice(scelte_tipo_ingaggio)
    lista_interventi.append([tecnico,
                             tipo_servizio,
                             richiedente,
                             data_richiesta,
                             tipo_ticket,
                             area_intervento,
                             descrizione_richiesta,
                             soluzione_adottata,
                             stato_intervento,
                             asset_id,
                             fk_beneficiario_id,
                             data_chiusura,
                             tipo_ingaggio])

# print(lista_interventi)


db = sqlite3.connect('../../gse.sqlite3')
cur = db.cursor()
cur.executemany(sql_intervento,(lista_interventi))
db.commit()
db.close()