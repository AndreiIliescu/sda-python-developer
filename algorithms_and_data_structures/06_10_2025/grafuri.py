""" Un graf este o structura de noduri formata din noduri + muchii
Poate fi orientat/neorientat, ponderat /neponderat
Este folosit in retele sociale, google maps, waze, organizare de trafic auto/trenuri/avioane

Pentru asincron in Python: asyncio, Celery
Celery = un framework Python pt. joburi asincrone si task-uri in background (de fapt este o 'coada')
Sincron/Asincron = despre cum astepti rezultatul unui task
Single-thread/Multithread = despre cate threads folosesti in rularea codului

mai jos exemplu cu Celery pe pasi:
1. Instalezi Celery și Redis

pip install celery redis


2. Creezi un fișier tasks.py:

from celery import Celery

# Configurăm aplicația Celery cu Redis ca broker
app = Celery('tasks', broker='redis://localhost:6379/0')

# Definim un task asincron
@app.task
def adunare(x, y):
    return x + y

3. Rulezi worker-ul Celery (într-un terminal separat):

celery -A tasks worker --loglevel=info

4. Apelezi task-ul din Python:

from tasks import adunare

rezultat = adunare.delay(4, 6)  # rulează asincron
print(rezultat.id)  # ID-ul taskului
print(rezultat.get())  # când e gata, returnează 10

Ce este Redis?

Redis este:

un sistem de stocare în memorie (in-memory data store),
foarte rapid
folosit de obicei ca bază de date, cache """
