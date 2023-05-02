import typing as t
from pydantic import BaseModel, Field


class ProjectSchema(BaseModel):
    id: int = Field(example=110)
    title: str = Field(example="Ferialabs Branding")
    description: str = Field(
        example="Website for a digital agency Feria Labs. Used for attracting clients and showing the portfolio of the company"
    )
    website_link: str = Field(example="https://ferialabs.com")
    body: str = Field(
        example="<body> <p>Some text about the project description goes here </p> <h1> A big title</h1>"
    )
