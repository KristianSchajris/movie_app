from typing import Optional
from pydantic import BaseModel, Field

class FullDataRequest(BaseModel):
    movie_title: str = Field(..., description="The title of the movie", examples=["Deadpool & Wolverine"])
    language: str = Field(..., description="The language for the request", examples=["en-US"])
    latitude: float = Field(..., description="Latitude coordinate", examples=[11.2361])
    longitude: float = Field(..., description="Longitude coordinate", examples=[-74.20167])
