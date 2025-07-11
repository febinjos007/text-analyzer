import pytest
from fastapi import HTTPException
from src.service import analyze_text


def test_analyze_text_positive_sentiment():
    text = "The trip was fantastic and the food was excellent!"
    result = analyze_text(text)

    assert result["word_count"] == 9
    assert (
        "fantastic" in result["most_common_words"]
        or "excellent" in result["most_common_words"]
    )
    assert result["sentiment"] == "positive"


def test_analyze_text_negative_sentiment():
    text = "It was a terrible experience and the food was awful"
    result = analyze_text(text)

    assert result["sentiment"] == "negative"


def test_analyze_text_neutral_sentiment():
    text = "This is a regular statement without strong emotions"
    result = analyze_text(text)

    assert result["sentiment"] == "neutral"
