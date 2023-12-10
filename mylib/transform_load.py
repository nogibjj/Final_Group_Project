"""
Transforms and Loads data into the local SQLite3 database

"""
import sqlite3
import csv


# load the csv file and insert into a new sqlite3 database
def load(dataset="data/spotify_songs.csv"):
    """Transforms and Loads data into the local SQLite3 database"""
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    # skips the header of csv
    next(payload)
    conn = sqlite3.connect("spotifyDB.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS spotifyDB")
    c.execute(
        """
        CREATE TABLE spotifyDB (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            track_name TEXT,
            artist(s)_name TEXT,
            artist_count INTEGER,
            released_year INTEGER,
            released_month INTEGER,
            released_day INTEGER,
            in_spotify_playlists INTEGER,
            in_spotify_charts INTEGER,
            streams INTEGER,
            in_apple_playlists INTEGER
        )
    """
    )
    # insert
    c.executemany(
        """
        INSERT INTO spotifyDB(
            track_name,
            artist(s)_name,
            artist_count,
            released_year,
            released_month,
            released_day,
            in_spotify_playlists,
            in_spotify_charts,
            streams,
            in_apple_playlists
            ) 
            VALUES (?,?, ?, ?, ?,?,?,?,?,?)""",
        payload,
    )
    conn.commit()
    conn.close()
    return "extract.db"
