import psycopg2 as pg
import sys
import os

DATABASE_URL = os.environ['DATABASE_URL']

def insert(values):
    con = None

    try:
        con = pg.connect(DATABASE_URL, sslmode='require')
        sql = "INSERT INTO measurement (\
                temperature,\
                pressure,\
                humidity,\
                co2ppm) VALUES (%s,%s,%s,%s)"
        with con:
            cur = con.cursor()
            cur.execute(sql, values)
    except pg.Error as e:
        print("Error %s:" % e.args[0])
        sys.exit(1)
    finally:
        if con:
            con.close()

def delete_old():
    try:
        con = pg.connect(DATABASE_URL, sslmode='require')
        with con:
            cur = con.cursor()
            cur.execute("DELETE FROM measurement WHERE\
                           id IN ( \
                               SELECT id FROM measurement WHERE \
                               created_at < NOW() - INTERVAL '4 DAYS' \
                            );")
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
                    id SERIAL PRIMARY KEY,\
                    temperature REAL,\
                    pressure REAL,\
                    humidity REAL,\
                    co2ppm REAL,\
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")
    except pg.Error as e:
        print("Error %s:" % e.args[0])
        sys.exit(1)
    finally:
        if con:
            con.close()

