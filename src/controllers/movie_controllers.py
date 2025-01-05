from fastapi import HTTPException, status
from src.schemas.full_data_request import FullDataRequest
from src.schemas.partial_data_request import PartialDataRequest
from src.services.movie_service import MovieService
from src.utils.webhook_utils import send_to_webhook


class MovieController:

    @staticmethod
    def search_movie_by_title(request: PartialDataRequest) -> dict:
        """
        This resource gets the detailed information of a movie based on the title.

        Args:
            request (PartialDataRequest): The request object containing the movie title and language.

        Returns:
            dict: A dictionary containing the movie details and HTTP status code.

        Raises:
            HTTPException: If the movie is not found (404) or if there is an internal server error (500).
        """
        try:
            movie = MovieService.search_movie_by_title(title=request.movie_title, language=request.language)

            if not movie:
                raise HTTPException(status_code=404, detail="Movie not found")

            send_to_webhook(movie)

            return {
                "response": movie,
                "status": status.HTTP_200_OK
            }
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


    @staticmethod
    def get_movie_and_weather_data(request: FullDataRequest) -> dict:
        """
        Get movie and weather data based on the title.

        Args:
            request (FullDataRequest): The request object containing the movie title, language, latitude, longitude, start date, and end date.

        Returns:
            dict: A dictionary containing the movie and weather data and HTTP status code.

        Raises:
            HTTPException: If there is an internal server error (500).
        """
        try:
            movie = MovieService.search_movie_by_title(title=request.movie_title, language=request.language)

            movie_and_weather_data = MovieService.get_movie_and_weather_data(
                title=movie['title'],
                language=movie['original_language'],
                latitude=request.latitude,
                longitude=request.longitude,
                start_date=movie['release_date'],
                end_date=movie['release_date']
            )

            send_to_webhook(movie_and_weather_data)

            return {
                "response": movie_and_weather_data,
                "status": status.HTTP_200_OK
            }
        except Exception as e:
            print(f"Error: {e}")
            raise HTTPException(status_code=500, detail=str(e))
