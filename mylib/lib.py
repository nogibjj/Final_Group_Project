import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statistics import mean

# This file includes all the functions created. 

def plot_popularity(data):
    # Create a figure with a custom size
    plt.figure(figsize=(12, 5))
    # Set the seaborn theme to darkgrid
    sns.set_theme(style='darkgrid')
    sns.histplot(data["track_popularity"], kde=True)
    # Add labels to the x-axis and y-axis
    plt.xlabel('Popularity', fontsize=14)
    plt.ylabel('Density', fontsize=14)
    # Add a title to the plot
    plt.title('Distribution of Track Popularity',fontsize=15)

def genre_count(data):
    # Count the number of tracks in each genre
    counts = data['playlist_genre'].value_counts()
    top_genre = counts.reset_index()
    top_genre.columns = ['Playlist Genre', 'Track Counts']
    return top_genre

def genre_popularity(data):
    # Set the figure size
    plt.figure(figsize=(12, 8))
    # Create the point plot
    sns.pointplot(x = 'playlist_genre', y='track_popularity', data=data, estimator = np.mean)
    # Add axis labels and a title
    plt.xlabel('Playlist Genre',fontsize=14)
    plt.ylabel('Average Popularity',fontsize=14)
    plt.title('Average Popularity by Music Genre',fontsize=15)

def month_popularity(data):
    data['track_album_release_date'] = data['track_album_release_date'].astype(str)
    # Filter out rows with different date formats
    data = data[pd.to_datetime(data['track_album_release_date'], errors='coerce').notna()]
    # Convert the 'track_album_release_date' column to datetime
    data['track_album_release_date'] = pd.to_datetime(data['track_album_release_date'])
    # Extract the month from the datetime values
    data['release_month'] = data['track_album_release_date'].dt.month_name()
    month_order = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    plt.figure(figsize=(12, 8))
    sns.pointplot(x='release_month',  y='track_popularity', data=data, palette='viridis',estimator = np.mean,order=month_order)
    # Set labels and title
    plt.xlabel('Release Month', fontsize=14)
    plt.ylabel('Average Track Popularity', fontsize=14)
    plt.title('Average Track Popularity by Month', fontsize=15)