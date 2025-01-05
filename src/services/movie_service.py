from src.utils.tmdb_utils import get_movie_details, get_movie_genres
from src.utils.weather_utils import get_weather_for_date


class MovieService:

    @staticmethod
    def search_movie_by_title(title: str, language: str) -> dict:
        """
        Search a movie by title

        Args:
            title (str): The title of the movie to search for.
            language (str): The language in which to search for the movie.
        Returns:
            dict: A dictionary containing the movie details.
        """

        movie = get_movie_details(title=title, language=language)
        movie['genres'] = get_movie_genres(movie['genre_ids'])
        movie.pop('genre_ids')
        movie.pop('id')

        return movie


    @staticmethod
    def get_movie_and_weather_data(title: str, language: str, latitude: float, longitude: float, start_date: str, end_date: str) -> dict:
        """
        Retrieve movie details and weather data for a specific date range.

            latitude (float): The latitude coordinate for the weather data.
            longitude (float): The longitude coordinate for the weather data.
            start_date (str): The start date for the weather data in 'YYYY-MM-DD' format.
            end_date (str): The end date for the weather data in 'YYYY-MM-DD' format.

            dict: A dictionary containing the movie details and weather data for the specified date range.

        Raises:
            ValueError: If the movie is not found.
        """
        movie_data = get_movie_details(title=title, language=language)

        if not movie_data:
            raise ValueError("This movie not found.")

        movie_data['genres'] = get_movie_genres(movie_data['genre_ids'])

        movie_data.pop('genre_ids')

        weather_data = get_weather_for_date(
            latitude=latitude,
            longitude=longitude,
            start_date=start_date,
            end_date=end_date
        )

        movie_data['release_day_weather'] = weather_data

        return movie_data
