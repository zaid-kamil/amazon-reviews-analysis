# amazon-reviews-analysis-api
A web API for an interactive dashboard where the user has options to scrape a new product review or to predict the sentiment overview of the already scraped product reviews.

### Features:
#### 1. Streamlit based interactive dashboard.
#### 2. Storing the new product reviews as a SQLite DB file and retrieving it later.
#### 1. Choice for fetching a new product review by providing the URL of the product web page. The product reviews are automatically scrapped using BeautifulSoup library.
#### 3. Choice for predicting the sentiment of already stored reivews with the help of Huggingface pretrained model.

## Files Information
### 1.main.py
#### The starting point of the project that provides an interface for different modules.

### 2.fetch_reviews.py
#### Contains the logic for fetching the user reviews by giving the product URL as an input.

### 3.sentiment_prediction.py
#### Contains the logic for sentiment prediction of review available for a product chosen from the drop-down menu.

### 4.requirements.txt
#### The file contains the list of all the required libraries
```bash
pip install -r requirements.txt
```


## Running Project
#### 1. Run the following command in the terminal of the IDE
####      	"`streamlit run main.py`"
#### 2. Click on the link shown after running the above command
#### 3. Select the action for fetching a new product review or predicting the sentiment of already fetched reviews from the drop-down menu and proceed as directed
