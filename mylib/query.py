"""Database query lib"""
import json
# import MySQLdb
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class DB:
    """DB utility class to connect and query ICU data"""
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),        # Use environment variable
            user=os.getenv("DB_USER"),        # Use environment variable
            passwd=os.getenv("DB_PASSWORD"),  # Use environment variable
            db=os.getenv("DB_NAME"),          # Use environment variable
            port=3306,    # Use environment variable (if needed)
        )
        self.cursor = self.connection.cursor()

    def get_song_info(self, track_id):
        """Return music info for a specified track"""
        query = f'SELECT track_id, track_name, track_artist, danceability, energy FROM spotify_songs WHERE track_id = "{track_id}"'
        self.cursor.execute(query)
        data = self.cursor.fetchall()

        result = [{'track_id': row[0], 'danceability':row[1] ,'energy': row[2],} for row in data]
        return json.dumps(result)


    def get_popularity_info(self):
        """Return summary info about track popularity"""
        query = 'SELECT genre, COUNT(*) FROM spotify_songs GROUP BY genre'
        self.cursor.execute(query)
        data = self.cursor.fetchall()

        result = [{'genre': row[0], 'count': row[1]} for row in data]
        return json.dumps(result)
