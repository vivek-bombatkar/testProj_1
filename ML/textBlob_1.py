from textblob import TextBlob

print(TextBlob("i am happy").sentiment.polarity)
print(TextBlob("i am happy").sentiment)
print(TextBlob("i am sad").sentiment)
print(TextBlob("i am nutral").sentiment)

print(TextBlob("ich bin vivek").detect_language().capitalize())
print(TextBlob("i am rebul").correct().translate(to="hi"))

print(TextBlob("i am happy and sad").tags)