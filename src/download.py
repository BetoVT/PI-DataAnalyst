from urllib.request import urlretrieve
import os
import csv

FILEPATH = "data\\raw\\"

def getLinks(read_obj):
    csv_reader = csv.reader(read_obj)
    list_of_csv = list(csv_reader)
    return list_of_csv

def getData(url, filename, ext):
    if os.path.exists(FILEPATH + filename + ext):
        os.remove(FILEPATH + filename + ext)
    print("Descargando de: " + url + filename + ext)
    urlretrieve(url + filename + ext, FILEPATH + filename + ext)
    print("Se termino de descargar de: " + url + filename + ext + "\n")

