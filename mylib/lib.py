import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
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

def plot_genre(data):
    # Set the figure size
    plt.figure(figsize=(12, 8))
    # Create a countplot of the genre data
    sns.countplot(x='playlist_genre', data=data)
    plt.xlabel('Playlist Genre', fontsize=14)
    plt.ylabel('Total Genre Counts', fontsize=14)
    plt.title('Playlist Genre Counts on Spotify', fontsize=15)

def genre_popularity(data):
    # Set the figure size
    plt.figure(figsize=(12, 8))
    # Create the point plot
    sns.pointplot(x = 'playlist_genre', y='track_popularity', data=data, estimator = np.mean)
    # Add axis labels and a title
    plt.xlabel('Playlist Genre',fontsize=14)
    plt.ylabel('Average Popularity',fontsize=14)
    plt.title('Average Popularity by Music Genre',fontsize=15)

