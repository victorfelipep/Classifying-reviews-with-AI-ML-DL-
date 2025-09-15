import pandas as pd
from transformers import pipeline
import matplotlib.pyplot as plt


#Load review .CSV file
df = pd.read_csv("base/reviews_example.csv")

#Load trained pipeline to classify reviews analysing sentiments multilingual
classifier = pipeline("sentiment-analysis",
                      model="nlptown/bert-base-multilingual-uncased-sentiment"
                    )

#Creating classification column
df["classification"] = None

#Classificating each review with transformers
for i in range(0, len(df["review_text"])):
    result = classifier(df.loc[i, "review_text"])[0]
    if result['label'] == "1 star" or result['label'] == "2 stars":
        df.loc[i, "classification"] = "NEGATIVE"
    elif result['label'] == "3 stars":
        df.loc[i, "classification"] = "NEUTRAL"
    else:
        df.loc[i, "classification"] = "POSITIVE"

#Save new .csv with classification column added
df.to_csv("classified_reviews.csv", index=False, encoding="utf-8-sig")
print("Saved succesfully")

#Create and display pie chart
value_counts = df["classification"].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Distribution of Categories')
plt.show()