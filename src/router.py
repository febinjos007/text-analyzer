from http import HTTPStatus

from fastapi import APIRouter, HTTPException, Request

from src.models import FeedbackResponse
from src.service import analyze_text

router = APIRouter()


@router.post(
    "/analyze",
    response_model=FeedbackResponse,
    responses={
        200: {"description": "Successful text analysis"},
        400: {"description": "Bad Request – input text was empty or invalid"},
        415: {"description": "Unsupported Media Type – only 'text/plain' allowed"},
        500: {"description": "Internal Server Error"},
    },
    summary="Analyze plain-text feedback",
    description="Accepts free-form plain text input, analyzes word frequency and sentiment.",
)
async def analyze_feedback(request: Request):
    """
    Analyze customer feedback text and return word count, most common words, and sentiment.

    Args:
        request: Simple free-form text
        Only accepts 'text/plain' content type.

    Returns:
        FeedbackResponse object with analysis results
    """

    body = await request.body()
    text = body.decode("utf-8").strip()

    # Check for empty input
    if not text:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail="Input text cannot be empty"
        )

    # Then check content type
    content_type = request.headers.get("content-type", "")
    if not content_type.startswith("text/plain"):
        raise HTTPException(
            status_code=HTTPStatus.UNSUPPORTED_MEDIA_TYPE,
            detail="Only 'text/plain' content is supported.",
        )

    result = analyze_text(text)
    return FeedbackResponse(**result)
