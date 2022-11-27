from fetch_reviews import get_review, get_available_files
from sentiment_prediction import get_sentiment_overview
import streamlit as st

if __name__ == '__main__':
    #  config

    st.image('https://dtmvamahs40ux.cloudfront.net/gl-academy/course/course-172-Sentiment%20Analysis%20of%20Amazon%20Reviews.jpg', use_column_width=True)
    st.title("Amazon Reviews Sentiment")
    choice = st.selectbox("Select Action", ("Scrape Reviews", "Predict Sentiment","check your review"))

    if "Scrape Reviews" == choice:
        st.write("Please copy the complete URL of the product page and paste below!")
        url = st.text_input("Product URL", help="url must contain the name of product after the amazon.com/, else you are selecting the wrong url")
        limit = st.number_input("Number of reviews to scrape", min_value=1, max_value=1000, value=100)
        if st.button('collect') and url:
            with st.spinner("Scraping reviews... this may take a while"):
                get_review(url, limit)
            st.write("Done!")
    elif "check your review" == choice:
        review = st.text_area("Enter your review")
        if st.button('predict') and review:
            with st.spinner("Predicting..."):
                st.write(get_sentiment_overview(review=review))
    else:
        files = get_available_files()
        file_choice = st.selectbox("Choose the review file for sentiment overview", files)

        button_choice = st.button('Predict Review Sentiment!')
        if button_choice:
            with st.spinner('Wait for it...'):
                get_sentiment_overview(file_choice)



# to run, open terminal run
#  streamlit run main.py