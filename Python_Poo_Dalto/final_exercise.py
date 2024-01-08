from textblob import TextBlob

class Sentiment_Analyzer:
  def sentiment_analyzer(self, text):
    analyzer = TextBlob(text)
    if analyzer.sentiment.polarity > 0:
      return "Positive"
    elif analyzer.sentiment.polarity == 0:
      return "neutral"
    else:
      return "negative"