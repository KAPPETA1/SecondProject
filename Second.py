import spacy 
from textblob import TextBlob
nlp=spacy.load("en_core_web_sm")
text="I thought the product would be great, but it was a complete disappointment. The packaging was damaged, and it looked nothing like the pictures online. It stopped working after just two days, and customer service was unresponsive. Honestly, I regret buying it and wouldn’t recommend it to anyone.This was the worst experience I’ve ever had. The service was painfully slow, the staff was rude, and the environment was filthy. Nothing worked as expected, and every promise turned out to be a lie. I felt ignored, disrespected, and completely let down. It was a total waste of time and money, and I would never go back or recommend it to anyone.This was the worst experience I’ve ever had. The service was painfully slow, the staff was rude, and the environment was filthy. Nothing worked as expected, and every promise turned out to be a lie. I felt ignored, disrespected, and completely let down. It was a total waste of time and money, and I would never go back or recommend it to anyone."
doc=nlp(text)
# or token in doc:
 #   print(token.text,token.pos_,token.dep_)
blob=TextBlob(text)
print(blob.sentiment)