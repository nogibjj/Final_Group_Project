"""
Extract a dataset from a URL
"""
import requests
import os

def extract(
    url="""
    https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023?select=spotify-2023.csv
    """,
    file_path="data/spotify_songs.csv",
    directory="data",
):
    """Extract a url to a file path"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path
