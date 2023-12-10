import pandas as pd
from unittest import mock, TestCase
import main

class TestMain(TestCase):

    @mock.patch('pandas.read_csv')
    @mock.patch('main.plot_popularity')
    @mock.patch('main.genre_count')
    @mock.patch('main.genre_popularity')
    @mock.patch('main.month_popularity')
    @mock.patch('main.find_highest_popularity_track')
    def test_main(self, mock_find_highest_popularity_track, mock_month_popularity, 
                  mock_genre_popularity, mock_genre_count, mock_plot_popularity, 
                  mock_read_csv):
        # Setup a mock DataFrame
        mock_df = pd.DataFrame({
            'track_id': ['1', '2'],
            'track_name': ['Song1', 'Song2'],
            'track_popularity': [50, 60],
            # Add other necessary columns
        })

        # Mock read_csv to return the mock DataFrame
        mock_read_csv.return_value = mock_df

        # Call the main function
        main.main()

        # Assertions to ensure each function was called
        mock_read_csv.assert_called_once_with("spotify_songs.csv")
        mock_plot_popularity.assert_called_once_with(mock_df)
        mock_genre_count.assert_called_once_with(mock_df)
        mock_genre_popularity.assert_called_once_with(mock_df)
        mock_month_popularity.assert_called_once_with(mock_df)
        mock_find_highest_popularity_track.assert_called_once_with(mock_df)

# This part is optional, to allow running tests from this script
if __name__ == '__main__':
    import unittest
    unittest.main()
