#!usr/bin/env python
import datetime
import pymongo
import requests


def create_record(lista):
    record = {
        'estacion':lista[0],
        'plataforma':lista[1],
        'datetime': set_datetime(lista[2],lista[3])
        'date':lista[2],
        'time':lista[3],
        'presion_atmosferica':float(lista[4]),
        'fuerza_viento':float(lista[5]),
        'direccion_viento':int(lista[6]),
        'temperatura':float(lista[7]),
        'lluvia':float(lista[8]),
        'lluvia_24h':float(lista[9])
    }
    return record

def set_datetime(date, time):
    date = [int(i) for i in date.split('-')]
    time = [int(i) for i in time.split(':')]
    complete = datetime.datetime(date[0], date[1], date[2], time[0], time[1], time[2])
    return complete

def parse_json(url):
    request = requests.get(url)
    json = request.json()
    return json

if __name__ == "__main__":
    json = parse_json("http://186.120.187.237/ema/join_data_24hrs.php")
    records=[]
    for item in json:
        record = create_record(item)
        record["utc_datetime"] = set_datetime

