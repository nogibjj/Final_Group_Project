"""
Transforms and Loads data into the local SQLite3 database

"""
import sqlite3
import csv


# load the csv file and insert into a new sqlite3 database
def load(dataset="data/births.csv"):
    """Transforms and Loads data into the local SQLite3 database"""
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    # skips the header of csv
    next(payload)
    conn = sqlite3.connect("birthDB.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS birthDB")
    c.execute(
        """
        CREATE TABLE birthDB (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            year INTEGER,
            month INTEGER,
            date_of_month INTEGER,
            day_of_week INTEGER,
            births INTEGER
        )
    """
    )
    # insert
    c.executemany(
        """
        INSERT INTO birthDB(
            year, 
            month,
            date_of_month, 
            day_of_week,
            births
            ) 
            VALUES (?,?, ?, ?, ?)""",
        payload,
    )
    conn.commit()
    conn.close()
    return "extract.db"
