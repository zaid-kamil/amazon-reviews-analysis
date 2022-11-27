import pandas
import os
from textblob import TextBlob
import streamlit as st
import re
import plotly.express as px

def get_sentiment_overview(file=None, review=None):
    if file:
        df = pandas.read_csv(os.path.join('available-reviews', file))
        # create rows from the content in column
        title = df['title']
        comments = df['comments']
        comments = df['comments'].str.split(',', expand=True).stack().reset_index()
        comments = comments.drop(columns=['level_0', 'level_1'])
        comments['title'] =df.title[0]
        comments.columns = ['comments', 'title']
        # clean the data
        comments['comments'] = comments['comments'].str.replace('[', '')
        comments['comments'] = comments['comments'].str.replace(']', '')
        comments['comments'] = comments['comments'].str.replace("'", '')
        comments['comments'] = comments['comments'].str.replace('"', '')
        # remove emojis
        comments['comments'] = comments['comments'].str.replace('[^\w\s#@/:%.,_-]', '', flags=re.UNICODE)
        # strip the data
        comments['comments'] = comments['comments'].str.strip()
        # remove empty rows
        comments = comments[comments['comments'] != '']
        with st.expander("View Reviews"): st.write(comments)

        # get sentiment
        comments['sentiment'] = comments['comments'].apply(lambda x: TextBlob(x).sentiment.polarity)
        # get sentiment overview
        vpositive = comments[comments['sentiment'] > 0.5]
        positive = comments[(comments['sentiment'] > 0.1) & (comments['sentiment'] <= 0.5)]
        neutral = comments[(comments['sentiment'] > -0.1) & (comments['sentiment'] <= 0.1)]
        negative = comments[(comments['sentiment'] > -0.5) & (comments['sentiment'] <= -0.1)]
        vnegative = comments[comments['sentiment'] <= -0.5]
        sentiment_overview = pandas.DataFrame({'Sentiment': ['Very Positive', 'Positive', 'Neutral', 'Negative', 'Very Negative'], 'Count': [len(vpositive), len(positive), len(neutral), len(negative), len(vnegative)]})
        sentiment_overview = sentiment_overview.set_index('Sentiment')
        
        # show chart
        st.subheader("Sentiment Overview")
        st.dataframe(sentiment_overview, use_container_width=True)
        c1, c2 = st.columns(2)
        fig = px.pie(sentiment_overview, values='Count', names=sentiment_overview.index, title='Sentiment Pie Chart', height=500)
        c1.plotly_chart(fig, use_container_width=True)
        fig = px.bar_polar(sentiment_overview, r='Count', theta=sentiment_overview.index, color=sentiment_overview.index, template='plotly_dark', title='Sentiment Polar Bar chart', height=500)
        c2.plotly_chart(fig, use_container_width=True)
    else:
        review_blob = TextBlob(review)
        entry = []
        for sentence in review_blob.sentences:
            entry.append([sentence, sentence.sentiment.polarity])
        df = pandas.DataFrame(entry, columns=['Sentence', 'Sentiment'])
        df['output'] = df['Sentiment'].apply(lambda x: 'Very Positive' if x > 0.5 else ('Positive' if x > 0.1 else ('Neutral' if x > -0.1 else ('Negative' if x > -0.5 else 'Very Negative'))))

        st.subheader("Sentiment Overview")
        st.dataframe(df, use_container_width=True)
        c1, c2 = st.columns(2)
        fig = px.pie(df, values='Sentiment', names='output', title='Sentiment Pie Chart', height=500)
        c1.plotly_chart(fig, use_container_width=True)
        fig = px.bar_polar(df, r='Sentiment', theta='output', color='output', template='plotly_dark', title='Sentiment Polar Bar chart', height=500)
        c2.plotly_chart(fig, use_container_width=True)