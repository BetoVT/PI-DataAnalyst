import pandas as pd
import os

TEST = True
FILEPATH = "Project\data\\processed\\"

def create_csv(filename, df):
    if os.path.exists("Project\data\\final\\" + filename):
        os.remove("Project\data\\final\\" + filename)
    df.to_csv("Project\data\\final\\" + filename, index=False)

def clean_homicides_facts():
    df = pd.read_csv(FILEPATH + "homicides_facts.csv")
    df.dropna(inplace=True)
    df.drop(df[df['victim_amount'] == "sd"].index, inplace = True)
    df.drop(df[df['fact_time'] == "SD"].index, inplace = True)
    create_csv("homicides_facts_clean.csv", df)

if TEST: 
    clean_homicides_facts()