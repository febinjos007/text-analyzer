import re
from collections import Counter
from http import HTTPStatus

from fastapi import HTTPException
from nltk.corpus import stopwords

from src.keywords import SENTIMENT_KEYWORDS


def analyze_text(text: str) -> dict:
    """
    Process input text and return analytics including word count, common words, and sentiment.
    """

    # Lowercase
    text_lower = text.lower()

    # Calculate word count
    word_count = len(text_lower.split())

    # Remove punctuations and stopwards
    punctuation_free_tokens = re.sub(r"[^\w\s']", "", text_lower).split()
    stop_words = set(stopwords.words("english"))
    stopwords_free_tokens = [
        token for token in punctuation_free_tokens if token not in stop_words
    ]

    # Get 3 most common
    # Counter is a subclass of dict specifically designed for counting hashable objects
    word_freq = Counter(stopwords_free_tokens)
    most_common = [word for word, _ in word_freq.most_common(3)]

    # Determine sentiment
    sentiment = "neutral"
    for sentiment_type, keywords in SENTIMENT_KEYWORDS.items():
        if any(keyword in text_lower for keyword in keywords):
            sentiment = sentiment_type
            break

    return {
        "word_count": word_count,
        "most_common_words": most_common,
        "sentiment": sentiment,
    }
