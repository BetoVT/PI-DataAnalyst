import pandas as pd
import os

FILEPATH = "data\\raw\\"

def process_accidents():
    df = pd.read_csv(FILEPATH + "AccidentesAviones.csv")
    #df.drop(columns=["ID", "AAAA", "MM", "DD", "HH", "LUGAR_DEL_HECHO",
    #                 "Altura", "Dirección Normalizada", "XY (CABA)",
    #                 "pos x", "pos y", "PARTICIPANTES"], inplace=True)
    #df.rename(columns={"N_VICTIMAS": "victim_amount",
    #                   "FECHA": "fact_date",
    #                   "ACUSADO": "accused"},
    #                   inplace=True)
    print(df)
    if os.path.exists("data\\processed\\accidents.csv"):
        os.remove("data\\processed\\accidents.csv")
    df.to_csv("data\\processed\\accidents.csv", index=False)


