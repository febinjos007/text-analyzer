import re
from collections import Counter

from nltk.corpus import stopwords

from src.keywords import NEGATION_WORDS, SENTIMENT_KEYWORDS


def analyze_text(text: str) -> dict:
    """
    Process input text and return analytics including word count, common words, and sentiment.
    """

    # Lowercase
    text_lower = text.lower()

    # Tokenize
    tokens = text_lower.split()

    # Calculate word count
    word_count = len(tokens)

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
    sentiment = __detect_sentiment(tokens=tokens)

    return {
        "word_count": word_count,
        "most_common_words": most_common,
        "sentiment": sentiment,
    }


def __detect_sentiment(tokens: list[str]) -> str:
    """
    Detects the sentiment of a tokenized input based on predefined sentiment keywords
    and nearby negation words.

    This function checks each token to see if it matches any known sentiment keywords
    (positive or negative). If a sentiment keyword is found, it also checks the three
    preceding tokens for the presence of negation words. If negation is detected, the
    sentiment is flipped.

    Args:
        tokens (list[str]): A list of lowercase word tokens from the input text.

    Returns:
        str: One of "positive", "negative", or "neutral" representing the detected sentiment.
    """
    for i, token in enumerate(tokens):
        for sentiment_type, keywords in SENTIMENT_KEYWORDS.items():
            if token in keywords:
                # Check for negation in previous 3 tokens
                previous_three_tokens = tokens[max(i - 3, 0) : i]
                if any(neg in previous_three_tokens for neg in NEGATION_WORDS):
                    return "negative" if sentiment_type == "positive" else "positive"
                return sentiment_type
    return "neutral"
