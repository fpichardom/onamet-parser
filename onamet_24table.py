#!usr/bin/env python
import datetime
from pymongo import MongoClient
import requests
import os.path

def create_record(lista):
    p_record = {
        'estacion':lista[0].strip(),
        'plataforma':lista[1].strip(),
        'datetime': set_datetime(lista[2].strip(), lista[3].strip()),
        'presion_atmosferica':check_float(lista[4]),
        'fuerza_viento':check_float(lista[5]),
        'direccion_viento':check_int(lista[6]),
        'temperatura':check_float(lista[7]),
        'lluvia':check_float(lista[8]),
        'lluvia_24h':check_float(lista[9])
    }
    return p_record

def set_datetime(date, time):
    try:
        date = [int(i) for i in date.split('-')]
        time = [int(i) for i in time.split(':')]
        complete = datetime.datetime(date[2], date[1], date[0], time[0], time[1], time[2])
        return complete
    except (ValueError,IndexError):
        return date+' '+time

def check_int(value):
    try:
        return int(value)
    except ValueError:
        return value
    
def check_float(value):
    try:
        return float(value)
    except ValueError:
        return value

def parse_json(url):
    request = requests.get(url)
    json = request.json()
    return json

def database_connection(uri, database, collection):
    client = MongoClient(uri)
    database = client[database]
    collection = database[collection]
    return collection
def write_result(result='success',error=''):
    if result == 'success':
        with open(os.path.join(os.path.expanduser('~'),'onamet24.log'), 'a') as outFile:
            outFile.write('Records write success:' + str(datetime.datetime.utcnow())+'\n')
    elif result == 'fail':
        with open(os.path.join(os.path.expanduser('~'),'onamet24.log'), 'a') as outFile:
            outFile.write('Records write failure:' + str(datetime.datetime.utcnow())+':Error-'+str(error)+'\n')
            
if __name__ == "__main__":
#records = [create_record(i) for i in json['aaData']]
    URI = 'mongodb://localhost:27017/'
    URL = 'http://186.120.187.237/ema/join_data_24hrs.php'
    DB = 'onamet'
    COL = 'onamet24h'
    try:
        JSON = parse_json(URL)
        CONN = database_connection(URI, DB, COL)
        for item in JSON['aaData']:
            CONN.insert_one(create_record(item))
        write_result()
    except ValueError as e:
        write_result('fail',e)
