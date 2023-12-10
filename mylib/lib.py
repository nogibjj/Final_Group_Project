import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from statistics import mean

def plot_popularity(data):
    plt.figure(figsize=(12, 5))
    sns.set_theme(style='darkgrid')
    sns.histplot(data["track_popularity"], kde=True)
    plt.xlabel('Popularity', fontsize=14)
    plt.ylabel('Density', fontsize=14)
    plt.title('Distribution of Track Popularity', fontsize=15)
    plt.savefig('popularity_distribution.png')
    plt.close()

def genre_count(data):
    counts = data['playlist_genre'].value_counts()
    top_genre = counts.reset_index()
    top_genre.columns = ['Playlist Genre', 'Track Counts']
    return top_genre

def genre_popularity(data):
    plt.figure(figsize=(12, 8))
    sns.pointplot(x='playlist_genre', y='track_popularity', data=data, estimator=mean)
    plt.xlabel('Playlist Genre', fontsize=14)
    plt.ylabel('Average Popularity', fontsize=14)
    plt.title('Average Popularity by Music Genre', fontsize=15)
    plt.savefig('genre_popularity.png')
    plt.close()

def month_popularity(data):
    data = data.copy()
    data['track_album_release_date'] = pd.to_datetime(data['track_album_release_date'], errors='coerce')
    data.dropna(subset=['track_album_release_date'], inplace=True)
    data['release_month'] = data['track_album_release_date'].dt.month_name()

    month_order = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]

    # Calculate the average popularity for each month
    avg_popularity_by_month = data.groupby('release_month')['track_popularity'].mean().reindex(month_order)
    
    # Plotting
    plt.figure(figsize=(12, 8))
    sns.pointplot(x=avg_popularity_by_month.index, y=avg_popularity_by_month.values, order=month_order)
    plt.xlabel('Release Month', fontsize=14)
    plt.ylabel('Average Track Popularity', fontsize=14)
    plt.title('Average Track Popularity by Month', fontsize=15)
    plt.savefig('monthly_popularity.png')
    plt.close()

    # Convert the result to a DataFrame for return
    popularity_trends = avg_popularity_by_month.reset_index()
    popularity_trends.columns = ['Release Month', 'Average Popularity']

    return popularity_trends


def find_highest_popularity_track(data):
    max_popularity = data['track_popularity'].max()
    most_popular_tracks = data[data['track_popularity'] == max_popularity]
    return most_popular_tracks[['track_name', 'track_artist', 'track_popularity']]
