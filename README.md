# Movie API

This project is a FastAPI application that provides movie information and weather data based on movie release dates and locations.

## Features

- Search movies by title
- Get weather information for a movie's release date at specific coordinates
- Simple web-based interface for movie search and display
- Automatic webhook notifications
- OpenAPI documentation (Swagger UI and ReDoc)

## Requisites

- Python 3.13.0
- pip (Python package installer)
- Git

## Installation

1. Clone the repository:
```bash
git clone https://github.com/KristianSchajris/movie_app.git
cd movie_app
```

2. Create a virtual environment:
```bash
python -m venv venv

On linux and Mac-OS use: source venv/bin/activate
On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
Create a `.env` file in the root directory with the following content:
```
TMDB_URL=tmdb_url
TMDB_API_KEY=tmdb_api_key
WEBHOOK_URL=webhook_url
HOST=127.0.0.1
PORT=8000
```

## Running the Application

1. Start the server:
```bash
uvicorn main:app --reload
```

2. Access the API and Interface:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
- Web Interface: http://127.0.0.1:8000/

## Interface

A simple web interface is provided to interact with the API. You can:


- **Search** for a movie by entering the movie title.
  - **Get information about the movie**, including:
  - The official title of the movie.
  - The genres of the movie.
  - Minimum and maximum temperatures on the date of release, in your city.

### To Access the Interface:

1. Open a web browser.
2. Navigate to `http://127.0.0.1:8000/`.
3. Type in the movie title in the search box and click "Search."
4. View details about the movie, including the title, genres, and weather information for the release date.

## API Endpoints

### POST /api/v1/movies/search-movie
Search for a movie by title.

### POST /api/v1/movies/get-movie-and-weather-data
Find information about your favorite movies and the maximum and minimum temperature in your city on the day of their release.

## Project Structure

```
├── app.py
├── main.py
├── requirements.txt
├── src/
│   ├── controllers/
│   ├── Helpers/
│   │   ├── fetch/
│   │   │    └── data_fetch.py
│   │   └── load_env/
│   │        └── load_env.py
│   ├── routers/
│   │    └── api
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   └── templates/
│       └── index.html
```
