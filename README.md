# Amazon Reviews Analysis

This project is designed to analyze Amazon product reviews by scraping review data from Amazon and performing sentiment analysis on the collected reviews. The project uses Python libraries such as `pandas`, `requests`, `BeautifulSoup`, `TextBlob`, and `Streamlit` to scrape and analyze the data and visualize the results.

## Table of Contents

- Introduction
- Features
- Installation
- Usage
  - Fetching Reviews
  - Sentiment Prediction
- Project Structure
- Contributing
- License

## Introduction

The Amazon Reviews Analysis project aims to provide an easy way to scrape Amazon product reviews, clean the data, and perform sentiment analysis to understand the overall sentiment of the reviews. The results are visualized using interactive charts and tables.

## Features

- **Scrape Amazon Reviews**: Fetch reviews from Amazon using the `fetch_reviews.py` script.
- **Sentiment Analysis**: Perform sentiment analysis on the reviews using the `sentiment_prediction.py` script.
- **Data Visualization**: Visualize the sentiment analysis results using interactive charts and tables.
- **Streamlit Interface**: A user-friendly interface to interact with the scripts using Streamlit.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/zaid-kamil/amazon-reviews-analysis.git
   cd amazon-reviews-analysis
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Fetching Reviews

To fetch reviews for a specific Amazon product, use the `fetch_reviews.py` script. This script scrapes the reviews and saves them in a CSV file.

Example usage:
```python
from fetch_reviews import get_review, get_available_files

# Fetch reviews for a specific product URL
url = "https://www.amazon.com/product-reviews/B08VRKTP28"
review_data = get_review(url, limit=100)

# List available review files
available_files = get_available_files()
print(available_files)
```

### Sentiment Prediction

To perform sentiment analysis on the fetched reviews, use the `sentiment_prediction.py` script. This script analyzes the sentiment of the reviews and visualizes the results using Streamlit.

Example usage:
```python
import streamlit as st
from sentiment_prediction import get_sentiment_overview

# Perform sentiment analysis on a review file
get_sentiment_overview(file="B08VRKTP28.csv")

# Perform sentiment analysis on a single review
review = "This product is amazing! I love it."
get_sentiment_overview(review=review)
```

### Streamlit Interface

To use the Streamlit interface, run the `main.py` script. This provides an interactive interface to scrape reviews and perform sentiment analysis.

Example usage:
```bash
streamlit run main.py
```

## Project Structure

- `fetch_reviews.py`: Contains functions to scrape Amazon reviews and save them in CSV files.
- `sentiment_prediction.py`: Contains functions to perform sentiment analysis on the reviews and visualize the results.
- `main.py`: Provides a Streamlit interface to interact with the scripts.
- `requirements.txt`: Lists the required Python packages for the project.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
