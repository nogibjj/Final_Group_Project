from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pandas as pd
from mylib.lib import find_most_popular_song, genre_count, genre_popularity

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
    song = find_most_popular_song(spotify_data)
    return {"most_popular_song": song}

@app.get("/genre_count")
def get_genre_count():
    count = genre_count(spotify_data)
    return {"genre_count": count}

# Add other endpoints as necessary
