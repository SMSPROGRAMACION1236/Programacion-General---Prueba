# from textblob import TextBlob

# class Sentiment_Analyzer:
#   def sentiment_analyzer(self, text):
#     analyzer = TextBlob(text)
#     if analyzer.sentiment.polarity > 0:
#       return "Positive"
#     elif analyzer.sentiment.polarity == 0:
#       return "neutral"
#     else:
#       return "negative"
  
# analyzer = Sentiment_Analyzer()
# result = analyzer.sentiment_analyzer("Glad ")
# print(result)

import openai

openai.api_key = "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"

system_role = """You are an analyzer of sentiments.
I give you a sentiment and you analyze the sentiment of the message and you return me a answer with 1 to 4 characters
Just numerical answer, where  -1 is the negative answer, 0 in neutral and 1 is the most positive
(you can just answer with ints or floats)"""

messages = [{"role": "system", "content": system_role}]

class Sentiment_Analyzer:
  def sentiment_analyzer(self, polarity):
    if polarity > -0.8 and polarity <= - 0.3:
      return "\x1b[1;31m" + "negative"  + "\x1b[0;37m" # Put a color
    elif polarity > -0.3 and polarity <- 0.1:
      return "\x1b[1;31m" + "Some negative" + "\x1b[0;37m"
    elif polarity >= -0.1 and polarity <= 0.1:
      return "\x1b[1;31m" + "neutral" + "\x1b[0;37m"
    elif polarity >= 0.1 and polarity <= 0.4:
      return "\x1b[1;31m" + "Some positive" + "\x1b[0;37m"
    elif polarity >= 0.4 and polarity <= 0.9:
      return "\x1b[1;31m" + "positive" + "\x1b[0;37m"
    elif polarity > 0.9:
      return "\x1b[1;31m" + "very positive " + "\x1b[0;37m"
    else:
      return "\x1b[1;31m" + "very negative" + "\x1b[0;37m"
analyzer = Sentiment_Analyzer()
while True:
  user_prompt = input("\x1b[1;31m" + "\nTell me something: " + "\x1b[0;37m")
  messages.append({"Role": "user", "content":user_prompt})
  completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = messages,
    max_tokens = 8
  )
  result = completion.choices[0].messages["content"]
  messages.append({"role":"assistant", "content": result})
  sentiment = analyzer.sentiment_analyzer(float(result))
  print(sentiment)