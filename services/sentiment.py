from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

def sentiment_analysis(text):
    score = sia.polarity_scores(text)
    return {
        "sentiment": "positive" if score["compound"] > 0.05 else
                     "negative" if score["compound"] < -0.05 else "neutral",
        "scores": score
    }
