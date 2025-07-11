from fastapi.testclient import TestClient
from src.main import app  # Replace with your actual FastAPI app import

client = TestClient(app)


def test_analyze_feedback_endpoint():
    response = client.post(
        "/analyze",
        data="The trip was awesome and quick!",
        headers={"Content-Type": "text/plain"},
    )

    assert response.status_code == 200
    data = response.json()
    assert data["word_count"] > 0
    assert isinstance(data["most_common_words"], list)
    assert data["sentiment"] == "positive"


def test_analyze_feedback_with_empty_input():
    response = client.post(
        "/analyze",
        data="   ",
        headers={"Content-Type": "text/plain"},
    )
    assert response.status_code == 400
    assert "Input text cannot be empty" in response.json()["detail"]


def test_analyze_feedback_negative_sentiment():
    response = client.post(
        "/analyze",
        data="The service was poor and very slow.",
        headers={"Content-Type": "text/plain"},
    )
    assert response.status_code == 200
    assert response.json()["sentiment"] == "negative"


def test_analyze_feedback_neutral_sentiment():
    response = client.post(
        "/analyze",
        data="This is a regular statement without strong emotions",
        headers={"Content-Type": "text/plain"},
    )
    assert response.status_code == 200
    assert response.json()["sentiment"] == "neutral"


def test_analyze_feedback_incorrect_content_type():
    response = client.post(
        "/analyze",
        data="This is a regular statement without strong emotions",
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 415
