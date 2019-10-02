import random
import string
import sys

import sqlite3

n_utenti = int(sys.argv[1])

divisione = ["Zuccheri semplici",
             "Zuccheri composti",
             "Dolcificanti",
             "Ricerca&Sviluppo",
             "Servizi&Logistica",
             ]

ruolo = ['dir', 'seg']

# funzione per generare un'utenza alfanumerica di 10 caratteri random
def utenza():
    utenza = "".join(random.choice(string.ascii_uppercase) for x in range(3)) + "".join(random.choice(string.digits) for x in range(7))
    return utenza

# funzione per generare una matricola numerica di 10 cifre random
def matricola():
    matricola = "".join(random.choice(string.digits) for x in range(10))
    return matricola


with open('nomi.txt') as nomi:
    lista_nomi = nomi.read()

with open('cognomi.txt') as cognomi:
    lista_cognomi = cognomi.read()



lista = []

for x in range(n_utenti):
    lista.append([str(random.choice(lista_nomi.split())).capitalize(),
                  str(random.choice(lista_cognomi.split(sep='\n'))).capitalize(),
                  matricola(),
                  random.choice(divisione),
                  random.choice(ruolo),
                  True,
                  utenza()],)


db = sqlite3.connect('../../gse.sqlite3')
sql = ('''INSERT INTO anagrafica_utente(nome,cognome,matricola,divisione,ruolo,attivo,utenza) VALUES(?,?,?,?,?,?,?)''')
cur = db.cursor()
cur.executemany(sql,(lista))
db.commit()
db.close()
# print(lista)



