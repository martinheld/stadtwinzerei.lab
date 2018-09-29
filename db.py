import sqlite3 as lite
import sys

DB_NAME='measurements.db'

def insert(values):
    con = None

    try:
        con = lite.connect(DB_NAME)
        sql = "INSERT INTO measurement (\
                temperature,\
                pressure,\
                humidity,\
                co2ppm) VALUES (?,?,?,?)"
        with con:
            cur = con.cursor()
            cur.execute(sql, values)
    except lite.Error as e:
        print("Error %s:" % e.args[0])
        sys.exit(1)
    finally:
        if con:
            con.close()

def create_table():
    try:
        con = lite.connect(DB_NAME)
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
    except lite.Error as e:
        print("Error %s:" % e.args[0])
        sys.exit(1)
    finally:
        if con:
            con.close()

