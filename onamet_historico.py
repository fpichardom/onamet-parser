#!usr/bin/env python

import datetime
from pymongo import MongoClient
import requests
#import os.path
#import json

#def export_json

def create_record(lista):
    p_record = {
        'estacion':lista[0].strip(),
        'datetime': set_datetime(lista[1].strip(), lista[2].strip()),
        'presionAtmosferica':float(lista[3]),
        'fuerzaViento':float(lista[4]),
        'direccionViento':int(lista[5]),
        'radiacionSolar':check_int(lista[6]),
        'temperatura':float(lista[7]),
        'humedadRelativa':int(lista[8]),
        'lluvia':float(lista[9])
    }
    return p_record

def set_datetime(date, time):
    date = [int(i) for i in date.split('-')]
    time = [int(i) for i in time.split(':')]
    complete = datetime.datetime(date[0], date[1], date[2], time[0], time[1], time[2])
    return complete

def parse_json(url):
    request = requests.get(url)
    json = request.json()
    return json

def database_connection(uri, database, collection):
    client = MongoClient(uri)
    database = client[database]
    collection = database[collection]
    return collection

def check_int(value):
    try:
        return int(value)
    except ValueError:
        return value

def format_url_historico(url,start,last):
    formated=url.format(start,last)
    return formated
def display_range(url,start,end,step):
    prev= 0
    last =0
    for i in range(start,end,step):
        if last == 0:
            last = i
        elif prev == 0 and last !=0:
            print(prev,last)
            print(format_url_historico(url,prev,last)
        elif prev != 0:
            prev = last+1
            last = i
            print(prev,last)
            print(format_url_historico(url,prev,last)


if __name__ == "__main__":
#records = [create_record(i) for i in json['aaData']]
    URI = 'mongodb://localhost:27017/'
    URL = 'http://186.120.187.237/ema/join_data_historico.php?iDisplayStart={}&iDisplayLength={}'
    DB = 'onamet'
    COL = 'onametHistorico'
    JSON = parse_json(URL)
    CONN = database_connection(URI, DB, COL)
    for item in JSON['aaData']:
        CONN.insert_one(create_record(item))

    for i in range(0,100000,20000):
        prev= None
        last = i
        if prev is None and last == 0:
            prev == 0
        elif prev == 0:
            print(prev,last)
            print(format_url_historico(URL,prev,last)
        elif prev != 0:
            prev = last+1
            last = i
            print(prev,last)
            print(format_url_historico(URL,prev,last)
