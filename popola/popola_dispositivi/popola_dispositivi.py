import sqlite3
import random
import string
from faker import Faker
import datetime

fake = Faker()

start_date = datetime.date(year=2010, month=1, day=1)
location = ["Torino", "Milano", "Roma","Amburgo", "Toronto", "Pechino",]
lista_dispositivi = []
lista = []

# funzione per generare un asset alfanumerico di 10 caratteri random
def asset():
    asset = "".join(random.choice(string.ascii_uppercase) for x in range(2)) + "".join(random.choice(string.digits) for x in range(8))
    return asset

# funzione per generare un seriale numerico di 10 cifre random
def seriale():
    seriale = "".join(random.choice(string.digits) for x in range(10))
    return seriale

db = sqlite3.connect('../../gse.sqlite3')
cur = db.cursor()
cur.execute("""SELECT id, fk_produttore_id, fk_tipo_dispositivo_id, modello FROM dispositivi_modello""")  # qui estrae tutti i modelli di dispositivo e ottengo "lista_dispositivi"

for row in cur:
    # dispositivi_modello = {"id": row[0], "fk_produttore_id": row[1], "fk_tipo_dispositivo_id": row[2], "modello": row[3] }
    dispositivi_modello = [row[0], row[1], row[2], row[3],]
    lista_dispositivi.append(dispositivi_modello)
    # print(dispositivi_modello)
db.close()

# print(random.choice(lista_dispositivi))

sql1 = """SELECT * FROM anagrafica_utente"""
sql2 = """INSERT INTO dispositivi_dispositivo (asset, tipo_dispositivo_id, seriale, data_installazione, produttore_id, modello_id, utente_id, location) VALUES (?,?,?,?,?,?,?,?)"""

db = sqlite3.connect('../../gse.sqlite3')
cur = db.cursor()
cur.execute(sql1)  # qui estrae tutti gli utenti per poterli ciclare qui sotto

for row in cur:
    d1= random.choice(lista_dispositivi) # qui sceglie una coppia di dispositivi random da assegnare allo stesso utente
    d2= random.choice(lista_dispositivi)

    rdm_location = random.choice(location)
    data_installazione = fake.date_between(start_date=start_date, end_date='today')  # qui genera una data random tra start_date e today
    lista.append([asset(),d1[2], seriale(), data_installazione, d1[1], d1[0], row[0], rdm_location])  # qui popolo "lista" per poterla passare alla query che carica i dispositivi
    lista.append([asset(),d2[2], seriale(), data_installazione, d2[1], d2[0], row[0], rdm_location])
    # print(row[0], rdm_location, seriale(), asset(), data_installazione, d1[0], d1[1], d1[2], d1[3])
    # print(row[0], rdm_location, seriale(), asset(), data_installazione, d2[0], d2[1], d2[2], d2[3])
db.close()

# print(lista)
db = sqlite3.connect('../../gse.sqlite3')
cur = db.cursor()
cur.executemany(sql2,(lista))
db.commit()
db.close()