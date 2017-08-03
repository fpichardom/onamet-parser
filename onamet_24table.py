#!usr/bin/env python

import pymongo
from bs4 import BeautifulSoup as bs
import requests

def get_table(url):
    r = requests.get(url)
    html_doc = r.content
    soup = bs(html_doc, "html.parser")
    table = soup.table
    return soup


class Climate_data(object):
    def __init__(self,
                 estacion,
                 plataforma,
                 date_time,
                 presion_atmosferica,
                 fuerza_viento,
                 direccion_viento,
                 temperatura,
                 lluvia,
                 lluvia_24h):
        self.estacion = estacion
        self.plataforma = plataforma
        self.date_time = date_time
        self.presion_atmosferica = float(presion_atmosferica)
        self.fuerza_viento = float(fuerza_viento)
        self.direccion_viento = int(direccion_viento)
        self.temperatura = float(temperatura)
        self.lluvia = float(lluvia)
        self.lluvia_24h = float(lluvia_24h)
if __name__ == "__main__":
    soup = get_table("http://186.120.187.237/ema/index.html")
