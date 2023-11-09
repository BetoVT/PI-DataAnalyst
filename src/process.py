import pandas as pd
import json

FILEPATH = "data\\raw\\"

def process_local_con():
    with open(FILEPATH + 'local_con.json', 'r') as fp:
        data = json.load(fp)

    headers = []
    iter_dict = {}
    full_list = []

    for i in range (12):
        headers.append(data['result']['fArray'][i]['fStr'])
    
    for i in range(12, len(data['result']['fArray']), 12):
        for j in range(len(headers)):
            if j == 0 or j == 1 or j == 2:
                temp = data['result']['fArray'][i + j]['fStr']
            elif data['result']['fArray'][i + j]['fStr'] == "SI":
                temp = True
            elif data['result']['fArray'][i + j]['fStr'] == "--":
                temp = False
            else:
                temp = None
            iter_dict[headers[j]] = temp
        full_list.append(iter_dict)
        iter_dict = {}
    df = pd.DataFrame.from_dict(full_list)
    df.to_csv("data\\processed\\local_con.csv")
    print(df)

def process_internet_provincia():
    df= pd.read_csv("data\\raw\\internet_provincia.csv",
                    usecols=['Año', 'Trimestre',
                             'Provincia', 'Accesos por cada 100 hogares'],
                    decimal=',')
    df.to_csv("data\\processed\\internet_provincia.csv")
    

def process_internet_total():
    df= pd.read_csv("data\\raw\\internet_total.csv",
                    usecols=['Año', 'Trimestre',
                             'Accesos por cada 100 hogares',
                             'Accesos por cada 100 hab'],
                    decimal=',')
    df.to_csv("data\\processed\\internet_total.csv")

#process_local_con()
process_internet_provincia()
process_internet_total()