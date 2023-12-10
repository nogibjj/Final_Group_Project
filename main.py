from mylib.lib import (plot_popularity,genre_count,genre_popularity,
                       month_popularity, find_highest_popularity_track)
import pandas as pd
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=8000,
    )

def save_data(connection, row):
    cursor = connection.cursor()
    track_id, *rest = row
    query = "INSERT INTO spotify VALUES (%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s,%s, %s, %s);"
    cursor.execute(query)
    connection.commit()

def save_all_data():
    df = pd.read_csv("./spotify_songs.csv", encoding="utf-8")
    connection = get_connection()
    for index, row in df.iterrows():
        try:
            save_data(connection, row)
        except Exception as e:
            print(e)
            continue
    connection.close()

def main():
    save_all_data()
    spotify = pd.read_csv("spotify_songs.csv")
    plot_popularity(spotify)
    genre_table = genre_count(spotify)
    print(genre_table)
    genre_popularity(spotify)
    month_popularity(spotify)
    find_highest_popularity_track(spotify)
    
if __name__ == "__main__":
    main()