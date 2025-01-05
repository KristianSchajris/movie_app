from typing import List

from src.helpers.load_env.load_env import LoadEnv
from src.helpers.fetch.data_fetch import DataFetch

def get_data(extra_url, params):
    """
    Fetches data from the TMDB API using the provided extra URL and parameters.

    Args:
        extra_url (str): The additional URL path to append to the base TMDB URL.
        params (dict): A dictionary of parameters to include in the API request.
    Returns:
        dict: The JSON response from the TMDB API.
    Raises:
        Exception: If there is an error during the data fetch process.
    """
    tmdb_url = LoadEnv("TMDB_URL")
    tmdb_api_key = LoadEnv("TMDB_API_KEY")

    params['api_key'] = tmdb_api_key.get_value()

    dataFetch = DataFetch(
        url=tmdb_url.get_value(),
        extra_url=extra_url,
        params=params
    )

    return dataFetch.get()


def get_movie_genres(genre_ids: List[int]) -> List[dict]:
    """
    Fetches the names of movie genres based on a list of genre IDs.
    
    Args:
        genre_ids (List[int]): A list of genre IDs to fetch the names for.
    Returns:
        List[dict]: A list of genre names corresponding to the provided genre IDs.
                    If a genre ID is not found, it will be ignored in the result.
                    If there is an error fetching the genres, an empty list is returned.
    """
    response = get_data('/genre/movie/list', {
        'language': 'en',
    })

    if 'genres' in response:
        genres = {genre['id']: genre['name'] for genre in response['genres']}
        genre_names = [genres[genre_id] for genre_id in genre_ids if genre_id in genres]
        return genre_names
    else:
        print("Error: Unable to fetch genres.")
        return []


def build_movie_details(movie: dict, genere_ids: dict) -> dict:
    """
    Constructs a dictionary containing detailed information about a movie.
    Args:
        movie (dict): A dictionary containing movie information.
        genere_ids (dict): A dictionary containing genre IDs.
    Returns:
        dict: A dictionary with detailed movie information including title, genre IDs, release date, 
              adult content flag, backdrop path, movie ID, original language, original title, overview, 
              popularity, poster path, video flag, vote average, and vote count.
    """
    return {
        'title': movie['title'],
        'genre_ids': genere_ids,
        'release_date': movie['release_date'],
        'adult': movie.get('adult', False),
        'backdrop_path': movie.get('backdrop_path', ''),
        'id': movie.get('id', 0),
        'original_language': movie.get('original_language', ''),
        'original_title': movie.get('original_title', ''),
        'overview': movie.get('overview', ''),
        'popularity': movie.get('popularity', 0.0),
        'poster_path': movie.get('poster_path', ''),
        'video': movie.get('video', False),
        'vote_average': movie.get('vote_average', 0.0),
        'vote_count': movie.get('vote_count', 0),
    }


def get_movie_details(title: str, language: str) -> dict:
    """
    Fetches movie details from the TMDB API based on the given title and language.

    Args:
        title (str): The title of the movie to search for.
        language (str): The language code for the movie details (e.g., 'en-US').
    Returns:
        dict: A dictionary containing the movie details if found, otherwise an empty dictionary.
    Raises:
        Exception: If there is an error in fetching data from the API.
    """
    response = get_data('/search/movie', {
        'query': title,
        'language': language,
    })
    
    if 'results' in response and response['results']:
        movie = response['results'][0]
        genre_ids = movie.get('genre_ids', [])

        return build_movie_details(movie=movie, genere_ids=genre_ids)
    else:
        print("Error: Unable to fetch movie details or movie not found.")
        return {}
