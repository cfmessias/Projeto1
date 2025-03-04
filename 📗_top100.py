import os
import pandas as pd
import plotly.express as px
import streamlit as st

# Caminho absoluto para o diretório atual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Caminho absoluto para os datasets
reviews_path = os.path.join(current_dir, 'dataset', 'customer reviews.csv')
top100_books_path = os.path.join(current_dir, 'dataset', 'Top-100 Trending Books.csv')

# Carregar os datasets
df_reviews = pd.read_csv(reviews_path)
df_top100_books = pd.read_csv(top100_books_path)

# Título da aplicação
st.title("Top 100 Trending Books Analysis")

# Slider para faixa de preço
max_price = st.slider("Price Range ($)", min_value=int(df_top100_books["book price"].min()), max_value=int(df_top100_books["book price"].max()), value=int(df_top100_books["book price"].max()))

# Filtrar os dados com base no valor do slider
df_books = df_top100_books[df_top100_books["book price"] <= max_price]

# Mostrar tabela filtrada
st.write(df_books.head(10))

# Criar gráficos
fig_years = px.bar(df_books["year of publication"].value_counts().sort_index(), title="Books Published Per Year")
fig_prices = px.histogram(df_books["book price"], title="Book Price Distribution")
fig_ratings = px.bar(df_books["rating"].value_counts().sort_index(), title="Ratings Distribution")

# Mostrar gráficos
st.plotly_chart(fig_years)
st.plotly_chart(fig_prices)
st.plotly_chart(fig_ratings)
