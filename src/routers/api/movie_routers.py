from fastapi import APIRouter

from src.schemas.full_data_request import FullDataRequest
from src.schemas.partial_data_request import PartialDataRequest


from src.controllers.movie_controllers import MovieController

api_movies_router = APIRouter(prefix="/api/v1/movies", tags=["movies"])

api_movies_router.add_api_route(
    path="/search-movie",
    endpoint=MovieController.search_movie_by_title,
    methods=["POST"],
    summary="Search movie by title",
    description="Search for a movie by title and retrieve detailed information.",
)

api_movies_router.add_api_route(
    path="/get-movie-and-weather-data",
    endpoint=MovieController.get_movie_and_weather_data,
    methods=["POST"],
    summary="Get movie data",
    description="Find information about your favorite movies and the maximum and minimum temperature in your city on the day of their release.",
)
