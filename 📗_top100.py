import os
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide")

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

# Slider para faixa de preço na sidebar
max_price = st.sidebar.slider("Price Range ($)", min_value=int(df_top100_books["book price"].min()), max_value=int(df_top100_books["book price"].max()), value=int(df_top100_books["book price"].max()))

# Sliders para intervalo de anos de publicação na sidebar
min_year, max_year = st.sidebar.slider("Year of Publication Range", min_value=int(df_top100_books["year of publication"].min()), max_value=int(df_top100_books["year of publication"].max()), value=(int(df_top100_books["year of publication"].min()), int(df_top100_books["year of publication"].max())))

# Filtrar os dados com base nos valores dos sliders
df_books = df_top100_books[(df_top100_books["book price"] <= max_price) & (df_top100_books["year of publication"] >= min_year) & (df_top100_books["year of publication"] <= max_year)]

# Mostrar tabela filtrada
st.write(df_books.head(10))

# Criar gráficos
fig_years = px.bar(df_books["year of publication"].value_counts().sort_index(), title="Books Published Per Year")
fig_prices = px.histogram(df_books["book price"], title="Book Price Distribution")
fig_ratings = px.bar(df_books["rating"].value_counts().sort_index(), title="Ratings Distribution")

# Mostrar gráficos lado a lado
col1, col2,col3 = st.columns(3)
with col1:
    st.plotly_chart(fig_years)
with col2:
    st.plotly_chart(fig_prices)
with col3:
    st.plotly_chart(fig_ratings)