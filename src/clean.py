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

def clean_homicides_victims():
    df = pd.read_csv(FILEPATH + "homicides_victims.csv")
    df.dropna(inplace=True)
    df.drop(df[df['role'] == "SD"].index, inplace = True)
    df.drop(df[df['victim'] == "SD"].index, inplace = True)
    df.loc[df["age"] == "SD", "age"] = -1
    df.loc[df["age"] == "sd", "age"] = -1
    create_csv("homicides_victims_clean.csv", df)

def clean_injuries_facts():
    df = pd.read_csv(FILEPATH + "injuries_facts.csv")
    df1 = df.loc[lambda df: df['alt_dir'] == 'SD']
    print(df1)
    create_csv("injuries_facts_clean1.csv", df1)
    df2 = df.loc[lambda df: df['alt_dir'] != 'SD']
    print(df2)
    create_csv("injuries_facts_clean2.csv", df2)

def clean_injuries_victims():
    df = pd.read_csv(FILEPATH + "injuries_victims.csv")
    df.dropna(inplace=True)
    df.drop(df[df['vehicle'] == "sd"].index, inplace = True)
    df.drop(df[df['vehicle'] == "SD"].index, inplace = True)
    df.loc[df['age'] == "sd", "age"] = -1
    df.loc[df['age'] == "SD", "age"] = -1
    create_csv("injuries_victims_clean.csv", df)

if TEST: 
    #clean_homicides_facts()
    #clean_homicides_victims()
    clean_injuries_facts()
    #clean_injuries_victims()