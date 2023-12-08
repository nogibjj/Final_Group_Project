from mylib.lib import plot_popularity,genre_count,plot_genre,genre_popularity
import pandas as pd

def main():
    spotify = pd.read_csv("spotify_songs.csv")
    plot_popularity(spotify)
    genre_table = genre_count(spotify)
    print(genre_table)
    plot_genre(spotify)
    genre_popularity(spotify)


if __name__ == "__main__":
    main()