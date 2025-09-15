# Product Review Sentiment Classifier

This project classifies product reviews from a CSV file using a pre-trained multilingual BERT model and saves a new CSV file with sentiment classifications. It also generates a pie chart to visualize the distribution of sentiment categories.

---

## Project Structure

/base/reviews_example.csv # Original CSV with product reviews
classified_reviews.csv # CSV generated with sentiment classifications
main.py # Main script to classify reviews and generate chart
README.md # Project documentation
requirements.txt


## Features

- Classifies reviews as **POSITIVE**, **NEUTRAL**, or **NEGATIVE** based on their sentiment.
- Supports multilingual text using `nlptown/bert-base-multilingual-uncased-sentiment`.
- Saves a new CSV file with an added `classification` column.
- Generates a pie chart showing the distribution of classifications.

---

## Installation

- Clone the repository
- Install required packages:

pip install pandas matplotlib transformers torch

## Usage
Place your review CSV file in the /base/ folder. The file should contain a column named review_text.

Run the classification script:

python main.py

The script will:

Read the reviews from /base/reviews_example.csv.

Classify each review as POSITIVE, NEUTRAL, or NEGATIVE.

Save the classified reviews to /classified/reviews.csv.

Display a pie chart with the distribution of classifications.

## Example
Input (reviews_example.csv):

review_text
"Great product, highly recommend!"
"Not satisfied with the quality."
"It's okay, nothing special."

Output (classified/reviews.csv):

review_text	classification
"Great product, highly recommend!"	POSITIVE
"Not satisfied with the quality."	NEGATIVE
"It's okay, nothing special."	NEUTRAL

## License
This project is created by Victor Souza for educational and portfolio purposes only.