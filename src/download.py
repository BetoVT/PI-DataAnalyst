import json
import requests
import os

#FILEPATH = "data\\raw\\"
API_KEY = 'UJEWjaPnY2FLu76fqL1goyUK1O0eoB56W3k9iiVN'


def download_local_con(): 
    response = requests.get("http://api.datosabiertos.enacom.gob.ar/api/v2/datastreams/LISTA-DE-LOCAL-CON-CONEC/data.json/?auth_key=" + API_KEY + "&limit=4312")

    if os.path.exists("data\\raw\\local_con.json"):
        os.remove("data\\raw\\local_con.json")

    with open('data/raw/local_con.json', 'w') as fp:
        json.dump(response.json(), fp)

def download_internet_total():
    response = requests.get("http://api.datosabiertos.enacom.gob.ar/api/v2/visualizations/PENET-POR-HOGAR-NACIO-DEL/?auth_key=" + API_KEY)
    
    if os.path.exists("data\\raw\\internet_total.json"):
        os.remove("data\\raw\\internet_total.json")

    with open('data/raw/internet_total.json', 'w') as fp:
        json.dump(response.json(), fp)

def download_internet_provincia():
    response = requests.get("http://api.datosabiertos.enacom.gob.ar/api/v2/visualizations/PENET-DE-INTER-FIJO-57760/?auth_key=" + API_KEY)
    
    if os.path.exists("data\\raw\\internet_provincia.json"):
        os.remove("data\\raw\\internet_provincia.json")

    with open('data/raw/internet_provincia.json', 'w') as fp:
        json.dump(response.json(), fp)

#download_local_con()
#download_internet_access()