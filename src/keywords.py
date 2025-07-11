# Static stopword list (subset of common English stopwords)
# This is an alternative to using nltk.corpus import stopwords.
# But since nltk provide a more comprehensive list that's used in this service
# STOPWORDS = {
#     'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
#     'he', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'was',
#     'were', 'will', 'with'
# }

# Sentiment keyword dictionaries
# Note: more keywords can be added in here, which will improve sentiment analysis

SENTIMENT_KEYWORDS = {
    "positive": {
        "great",
        "awesome",
        "excellent",
        "good",
        "quick",
        "easy",
        "fantastic",
        "amazing",
    },
    "negative": {
        "bad",
        "poor",
        "slow",
        "terrible",
        "awful",
        "disappointing",
    },
}

NEGATION_WORDS = {
    "not",
    "never",
    "no",
    "n't",
}
