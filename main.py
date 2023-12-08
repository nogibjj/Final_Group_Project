from mylib.lib import plot_popularity,genre_count,genre_popularity,month_popularity
import pandas as pd
import matplotlib.pyplot as plt

def main():
    spotify = pd.read_csv("spotify_songs.csv")
    plot_popularity(spotify)
    genre_table = genre_count(spotify)
    print(genre_table)
    genre_popularity(spotify)
    month_popularity(spotify)
    
if __name__ == "__main__":
    main()