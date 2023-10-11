import mysql.connector
import pandas as pd

TEST = True
FILEPATH = "Project\data\\final\\"

def connect_db():
    mydb = mysql.connector.connect(host="localhost",
                                   user="root",
                                   password="260898",
                                   database="pi_da")
    return mydb

def create_tables(mydb):
    mycursor = mydb.cursor()
    mycursor.execute("DROP TABLE IF EXISTS homicides_facts")
    command = ("CREATE TABLE homicides_facts (" +
               "`id` INT NOT NULL AUTO_INCREMENT," +
               "`victim_amount` INT NULL," +
               "`fact_date` DATE NULL," +
               "`fact_time` TIME NULL," +
               "`street_type` VARCHAR(10) NULL," +
               "`street_name` VARCHAR(255) NULL," +
               "`cross_name` VARCHAR(255) NULL," +
               "`comuna` INT NULL," + 
               "`victim` VARCHAR(15) NULL," + 
               "`accused` VARCHAR(15) NULL," +
               "PRIMARY KEY (`id`));")
    mycursor.execute(command)
    mydb.commit()

def load_db(mydb):
    mycursor = mydb.cursor()
    command = ("INSERT INTO homicides_facts (victim_amount, fact_date, fact_time, " +
               "street_type, street_name, cross_name, comuna, victim, accused)" +
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
    df = pd.read_csv(FILEPATH + "homicides_facts_clean.csv")
    mycursor.executemany(command, df.values.tolist())
    mydb.commit()

if TEST:
    mydb = connect_db()
    #create_tables(mydb)
    #load_db(mydb)