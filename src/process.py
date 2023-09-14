import pandas as pd
import os

TEST = True
FILEPATH = "Project\data\\raw\\"

def create_csv(filename, df):
    if os.path.exists("Project\data\\processed\\" + filename):
        os.remove("Project\data\\processed\\" + filename)
    df.to_csv("Project\data\\processed\\" + filename, index=False)

def process_homicides_facts():
    df = pd.read_excel(FILEPATH + "homicides.xlsx", sheet_name="HECHOS")
    df.drop(columns=["ID", "AAAA", "MM", "DD", "HH", "LUGAR_DEL_HECHO",
                     "Altura", "Dirección Normalizada", "XY (CABA)",
                     "pos x", "pos y", "PARTICIPANTES"], inplace=True)
    df.rename(columns={"N_VICTIMAS": "victim_amount",
                       "FECHA": "fact_date",
                       "HORA": "fact_time",
                       "TIPO_DE_CALLE": "street_type",
                       "Calle": "street_name",
                       "Cruce": "cross_name",
                       "COMUNA": "comuna",
                       "VICTIMA": "victim",
                       "ACUSADO": "accused"},
                       inplace=True)
    create_csv("homicides_facts.csv", df)

def process_homicides_victims():
    df = pd.read_excel(FILEPATH + "homicides.xlsx", sheet_name="VICTIMAS")
    df.drop(columns=["ID_hecho", "AAAA", "MM", "DD", "FECHA_FALLECIMIENTO"], inplace=True)
    df.rename(columns={"FECHA": "victim_date",
                       "ROL": "role",
                       "VICTIMA": "victim",
                       "SEXO": "sex",
                       "EDAD": "age"},
                       inplace=True)
    create_csv("homicides_victims.csv", df)

def process_injuries_facts():
    df = pd.read_excel(FILEPATH + "injuries.xlsx", sheet_name="HECHOS")
    df.drop(columns=["id", "aaaa", "mm", "dd", "franja_hora",
                     "direccion_normalizada", "altura",
                     "geocodificacion_CABA", "longitud", "latutid",
                     "participantes"], inplace=True)
    df.rename(columns={"n_victims": "victim_amount",
                       "fecha": "fact_date",
                       "hora": "fact_time",
                       "tipo_calle": "street_type",
                       "otra_direccion": "alt dir",
                       "calle": "street_name",
                       "cruce": "cross_name",
                       "victima": "victim",
                       "acusado": "accused",
                       "moto": "bike",
                       "auto": "car",
                       "transporte_publico": "pub_transp",
                       "camion": "bus",
                       "ciclista": "cyclist",
                       "gravedad": "severity"},
                       inplace=True)
    create_csv("injuries_facts.csv", df)

def process_injuries_victims():
    df = pd.read_excel(FILEPATH + "injuries.xlsx", sheet_name="VICTIMAS")
    df.drop(columns=["ID hecho", "AAA", "MM", "DD"], inplace=True)
    df.rename(columns={"FECHA": "victim_date",
                       "VEHICULO_VICTIMA": "vehicle",
                       "SEXO": "sex",
                       "EDAD_VICTIMA": "age",
                       "GRAVEDAD": "severity"},
                       inplace=True)
    create_csv("injuries_victims.csv", df)


if TEST:
    process_homicides_facts()
    process_homicides_victims()
    process_injuries_facts()
    process_injuries_victims()


