from pydantic import BaseModel, Field

class PartialDataRequest(BaseModel):
    movie_title: str = Field(...,description="Title of the movie to search for", examples=["Inception"])
    language: str = Field(..., description="Language of the movie", examples=["en-US"])
