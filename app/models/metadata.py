from typing import List

from pydantic import BaseModel, Field


class MetadataOutput(BaseModel):
    """
    Metadata extracted from a research paper.
    """

    title: str = "Not specified in the paper."

    authors: List[str] = Field(default_factory=list)

    abstract: str = "Not specified in the paper."

    keywords: List[str] = Field(default_factory=list)

    institution: str = "Not specified in the paper."

    department: str = "Not specified in the paper."

    year: str = "Not specified in the paper."

    venue: str = "Not specified in the paper."

    domain: str = "Not specified in the paper."

    doi: str = "Not specified in the paper."

    emails: List[str] = Field(default_factory=list)

    language: str = "Not specified in the paper."

    pages: int = 0