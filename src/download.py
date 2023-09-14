from urllib.request import urlretrieve
import os
import csv

FILEPATH = "Project\data\\raw\\"

def getLinks(read_obj):
    csv_reader = csv.reader(read_obj)
    list_of_csv = list(csv_reader)
    return list_of_csv

def getData(url, filename, ext):
    if os.path.exists(FILEPATH + filename + ext):
        os.remove(FILEPATH + filename + ext)
    print("Descargando de: " + url + ext)
    urlretrieve(url + ext, FILEPATH + filename + ext)
    print("Se termino de descargar de: " + url + ext + "\n")

