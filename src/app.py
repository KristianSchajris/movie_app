import os
import uvicorn

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader

from src.helpers.load_env.load_env import LoadEnv
from src.routers.api.movie_routers import api_movies_router

class App:
    def __init__(self) -> None:
        self.app: FastAPI = FastAPI(
            title="Movie API",
            description="This is a simple API to get movie information",
            version="1.0.0",
            openapi_url="/api/v1/openapi.json",
            docs_url="/docs",
            redoc_url="/redoc"
        )

        self.host = LoadEnv("HOST").get_value()
        self.port = int(LoadEnv("PORT").get_value())

        self.templates = Environment(loader=FileSystemLoader("src/templates"))

        self.load_config()
        self.setup_docs()
        self.setup_api_routes()
        self.setup_routes()

    @property
    def asgi_app(self) -> FastAPI:
        return self.app

    def load_config(self) -> None:
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    async def custom_swagger_ui_html(self) -> HTMLResponse:
        return get_swagger_ui_html(
            openapi_url=self.app.openapi_url,
            title=self.app.title + " - Swagger UI",
            swagger_js_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.9.0/swagger-ui-bundle.js",
            swagger_css_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5.9.0/swagger-ui.css",
        )

    async def redoc_html(self) -> HTMLResponse:
        return get_redoc_html(
            openapi_url=self.app.openapi_url,
            title=self.app.title + " - ReDoc",
            redoc_js_url="https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js",
        )

    def setup_docs(self) -> None:
        self.app.add_api_route("/docs", self.custom_swagger_ui_html, include_in_schema=False)
        self.app.add_api_route("/redoc", self.redoc_html, include_in_schema=False)

    def setup_api_routes(self) -> None:
        self.app.include_router(api_movies_router)

    def setup_routes(self) -> None:
        @self.app.get("/", response_class=HTMLResponse)
        async def home(request: Request):
            api_url = "http://127.0.0.1:8000/api/v1/movies"

            fields = [
                {"id": "movie-title", "name": "movie-title", "type": "text", "label": "Movie Title", "placeholder": "E.g., Inception"},
                {"id": "language", "name": "language", "type": "text", "label": "Language", "placeholder": "E.g., en-US"},
                {"id": "latitude", "name": "latitude", "type": "number", "label": "Latitude", "placeholder": "E.g., 37.7749", "step": "any"},
                {"id": "longitude", "name": "longitude", "type": "number", "label": "Longitude", "placeholder": "E.g., -122.4194", "step": "any"}
            ]

            result_elements = [
                {"id": "result-title", "class": "mt-2 text-gray-800"},
                {"id": "result-genres", "class": "mt-2 text-gray-800"},
                {"id": "result-release-date", "class": "mt-2 text-gray-800"},
                {"id": "result-adult", "class": "mt-2 text-gray-800"},
                {"id": "result-backdrop-path", "class": "mt-2 text-gray-800"},
                {"id": "result-original-language", "class": "mt-2 text-gray-800"},
                {"id": "result-original-title", "class": "mt-2 text-gray-800"},
                {"id": "result-overview", "class": "mt-2 text-gray-800"},
                {"id": "result-popularity", "class": "mt-2 text-gray-800"},
                {"id": "result-poster-path", "class": "mt-2 text-gray-800"},
                {"id": "result-video", "class": "mt-2 text-gray-800"},
                {"id": "result-vote-average", "class": "mt-2 text-gray-800"},
                {"id": "result-vote-count", "class": "mt-2 text-gray-800"},
                {"id": "result-weather", "class": "mt-2 text-gray-800"}
            ]

            template = self.templates.get_template("index.html")
            content = template.render(title=self.app.title, fields=fields, api_url=api_url, result_elements=result_elements)
            return HTMLResponse(content=content)


    def start(self) -> None:
        uvicorn.run(self.app, host=self.host, port=self.port, log_level="info", reload=True)
