import mysql.connector
import pandas as pd

TEST = True
FILEPATH = "data\\processed\\"

def connect_db():
    mydb = mysql.connector.connect(host="localhost",
                                   user="root",
                                   password="260898",
                                   database="pi_da")
    return mydb

def create_tables(mydb):
    mycursor = mydb.cursor()
    mycursor.execute("DROP TABLE IF EXISTS internet_total")
    command = ("CREATE TABLE internet_total (" +
               "`id` INT NOT NULL AUTO_INCREMENT," +
               "`year` INT NULL," +
               "`trimester` INT NULL," + 
               "`access_homes` FLOAT NULL," + 
               "`access_person` FLOAT NULL," +
               "PRIMARY KEY (`id`));")
    mycursor.execute(command)
    mycursor.execute("DROP TABLE IF EXISTS internet_provincia")
    command = ("CREATE TABLE internet_provincia (" +
               "`id` INT NOT NULL AUTO_INCREMENT," +
               "`year` INT NULL," +
               "`trimester` INT NULL," + 
               "`provincia` VARCHAR(25) NULL," + 
               "`access_homes` FLOAT NULL," +
               "PRIMARY KEY (`id`));")
    mycursor.execute(command)
    mydb.commit()

def load_db(mydb):
    mycursor = mydb.cursor()
    command = ("INSERT INTO internet_total (year, trimester, access_homes, " +
               "access_person) VALUES (%s, %s, %s, %s)")
    df = pd.read_csv(FILEPATH + "internet_total.csv",
                     usecols=['Año', 'Trimestre',
                              'Accesos por cada 100 hogares',
                              'Accesos por cada 100 hab'])
    mycursor.executemany(command, df.values.tolist())
    mydb.commit()

if TEST:
    mydb = connect_db()
    create_tables(mydb)
    load_db(mydb)