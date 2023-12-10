CREATE TABLE icu_beds (
    track_id VARCHAR(255) NOT NULL,
    track_name TEXT,
    track_artist TEXT,
    track_popularity INTEGER,
    track_album_id VARCHAR,
    track_album_name TEXT,
    track_album_release_date TEXT,
    playlist_name TEXT,
    playlist_id VARCHAR,
    playlist_genre TEXT,
    playlist_subgenre TEXT,
    danceability DECIMAL,
    energy DECIMAL,
    key INTEGER,
    loudness DECIMAL,
    mode INTEGER,
    speechiness DECIMAL,
    acousticness DECIMAL,
    instrumentalness DECIMAL,
    liveness DECIMAL,
    valence DECIMAL,
    tempo DECIMAL,
    duration_ms INTEGER
    PRIMARY KEY (track_id)
);