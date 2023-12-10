from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import pandas as pd
from mylib.lib import (
    plot_popularity, genre_count, find_most_popular_genre, 
    month_popularity, find_highest_popularity_track
)

# Initialize the FastAPI app
app = FastAPI()

# Mount the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Instantiate the Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Load the Spotify dataset
spotify_data = pd.read_csv("spotify_songs.csv")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Render the index.html template
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/most_popular_song")
def get_most_popular_song():
    song = find_highest_popularity_track(spotify_data)
    return {"most_popular_song": song}

@app.get("/most_popular_genre")
def get_most_popular_genre():
    genre = find_most_popular_genre(spotify_data)  # This function needs to be implemented in lib.py
    return {"most_popular_genre": genre}

@app.get("/popularity_trends_by_month")
def get_popularity_trends_by_month():
    trends = month_popularity(spotify_data)
    # Convert DataFrame to JSON-friendly format
    return trends.to_dict('records')

# Add other endpoints as necessary
