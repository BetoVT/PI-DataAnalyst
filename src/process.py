import pandas as pd
import os

TEST = True
FILEPATH = "\data\\raw\\"

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


if TEST:
    print()
    #process_population()


