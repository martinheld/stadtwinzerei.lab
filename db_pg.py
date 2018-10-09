import psycopg2 as pg
import sys
import os

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

def insert(values):
    con = None

    try:
        con = pg.connect(DATABASE_URL, sslmode='require')
        sql = "INSERT INTO measurement (\
                temperature,\
                pressure,\
                humidity,\
                co2ppm) VALUES (?,?,?,?)"
        with con:
            cur = con.cursor()
            cur.execute(sql, values)
    except pg.Error as e:
        print("Error %s:" % e.args[0])
        sys.exit(1)
    finally:
        if con:
            con.close()

def create_table():
    try:
        con = pg.connect(DATABASE_URL, sslmode='require')
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS\
                measurement (\
                    id INTEGER PRIMARY KEY AUTOINCREMENT,\
                    temperature DOUBLE,\
                    pressure DOUBLE,\
                    humidity DOUBLE,\
                    co2ppm DOUBLE,\
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")
    except pg.Error as e:
        print("Error %s:" % e.args[0])
        sys.exit(1)
    finally:
        if con:
            con.close()

