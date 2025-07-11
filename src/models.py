# Pydantic models for response
from typing import List

from pydantic import BaseModel


class FeedbackResponse(BaseModel):
    word_count: int
    most_common_words: List[str]
    sentiment: str
