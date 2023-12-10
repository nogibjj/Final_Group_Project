"""Query the database"""

import sqlite3

# Define a global variable for the log file
LOG_FILE = "query_log.md"


def log_query(query):
    """adds to a query markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")


def general_query(query):
    """runs a query a user inputs"""
    # Connect to the SQLite database
    conn = sqlite3.connect("spotifyDB.db")

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Execute the query
    cursor.execute(query)

    # If the query modifies the database, commit the changes
    if (
        query.strip().lower().startswith("insert")
        or query.strip().lower().startswith("update")
        or query.strip().lower().startswith("delete")
    ):
        conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    log_query(f"{query}")


def create_record(
   track_name,
   artist(s)_name,
   artist_count,
   released_year,
   released_month,
   released_day,
   in_spotify_playlists,
   in_spotify_charts,
   streams,
   in_apple_playlists,
):
    """create example query"""
    conn = sqlite3.connect("spotifyDB.db")
    c = conn.cursor()
    c.execute(
        """
        INSERT INTO spotifyDB
        (track_name,
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
         VALUES (?,?, ?, ?, ?,?,?,?,?,?)
        """,
        (
         track_name,
         artist(s)_name,
         artist_count,
         released_year,
         released_month,
         released_day,
         in_spotify_playlists,
         in_spotify_charts,
         streams,
         in_apple_playlists,
        ),
    )
    conn.commit()
    conn.close()

    # Log the query
    log_query(
        f"""INSERT INTO spotifyDB VALUES (
            {track_name}, 
            {artist(s)_name},
            {artist_count}, 
            {released_year}, 
            {released_month},
            {released_day},
            {in_spotify_playlists},
            {in_spotify_charts},
            {streams},
            {in_apple_playlists});"""
    )


def update_record(
   track_name,
   artist(s)_name,
   artist_count,
   released_year,
   released_month,
   released_day,
   in_spotify_playlists,
   in_spotify_charts,
   streams,
   in_apple_playlists,
):
    """update example query"""
    conn = sqlite3.connect("spotifyDB.db")
    c = conn.cursor()
    print(
        (track_name,
   artist(s)_name,
   artist_count,
   released_year,
   released_month,
   released_day,
   in_spotify_playlists,
   in_spotify_charts,
   streams,
   in_apple_playlists,
        )
    )
    c.execute(
        """
        UPDATE spotifyDB 
        SET track_name = ?,
   artist(s)_name = ?,
   artist_count = ?,
   released_year = ?,
   released_month = ?,
   released_day = ?,
   in_spotify_playlists = ?,
   in_spotify_charts = ?,
   streams = ?,
   in_apple_playlists=?
        WHERE id=?;
        """,
        (
            track_name,
   artist(s)_name,
   artist_count,
   released_year,
   released_month,
   released_day,
   in_spotify_playlists,
   in_spotify_charts,
   streams,
   in_apple_playlists,
        ),
    )

    conn.commit()
    conn.close()

    # Log the query
    log_query(
        f"""UPDATE spotifyDB SET 
        track_name={track_name}, 
        artist(s)_name={artist(s)_name},
        artist_count={artist_count},
        released_year={released_year}, 
        released_day={released_day},
        in_spotify_playlists={in_spotify_playlists},
        in_spotify_charts={in_spotify_charts},
        streams={streams},
        in_apple_playlists={in_apple_playlists}
        WHERE id={record_id};"""
    )


def delete_record(record_id):
    """delete example query"""
    conn = sqlite3.connect("spotifyDB.db")
    c = conn.cursor()
    c.execute("DELETE FROM spotifyDB WHERE id=?", (record_id,))
    conn.commit()
    conn.close()

    # Log the query
    log_query(f"DELETE FROM spotifyDB WHERE id={record_id};")


def read_data():
    """read data"""
    conn = sqlite3.connect("spotifyDB.db")
    c = conn.cursor()
    c.execute("SELECT * FROM spotifyDB")
    data = c.fetchall()
    log_query("SELECT * FROM spotifyDB;")
    return data
