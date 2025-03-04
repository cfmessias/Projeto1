# https://www.kaggle.com/datasets/anshtanwar/top-200-trending-books-with-reviews
# Nov 23

import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(layout="wide")

df_reviews = pd.read_csv("dataset/customer reviews.csv")
df_top100_books = pd.read_csv("dataset/Top-100 Trending Books.csv")

price_max = df_top100_books["book price"].max()
price_min = df_top100_books["book price"].min()
max_price = st.sidebar.slider("Price Range", price_min, 
                      price_max, price_max, format="$%f")

df_books = df_top100_books[df_top100_books["book price"] <= max_price]
st.dataframe(df_books)

fig = px.bar(df_books["year of publication"].value_counts().sort_index())
fig2 = px.histogram(df_books["book price"])
fig3 = px.bar(df_books["rating"].value_counts().sort_index())

col1, col2, col3 = st.columns(3)
col1.plotly_chart(fig)
col2.plotly_chart(fig2)
col3.plotly_chart(fig3)
