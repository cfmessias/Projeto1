import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Carregar os datasets
df_reviews = pd.read_csv("dataset/customer reviews.csv")
df_top100_books = pd.read_csv("dataset/Top-100 Trending Books.csv")

# Inicializar a aplicação Dash
app = dash.Dash(__name__)

# Layout da aplicação
app.layout = html.Div([
    html.H1("Top 100 Trending Books Analysis", style={"textAlign": "center"}),
    
    html.Label("Price Range ($)"),
    dcc.Slider(
        id="price-slider",
        min=df_top100_books["book price"].min(),
        max=df_top100_books["book price"].max(),
        step=1,
        value=df_top100_books["book price"].max(),
        marks={int(price): f"${int(price)}" for price in df_top100_books["book price"].unique()[::10]},
    ),
    
    html.Div(id="filtered-table"),
    
    html.Div([
        dcc.Graph(id="year-publication-chart"),
        dcc.Graph(id="price-histogram"),
        dcc.Graph(id="rating-chart")
    ], style={"display": "flex", "justify-content": "space-around"})
])

# Callback para atualizar os dados filtrados e gráficos
@app.callback(
    [Output("filtered-table", "children"),
     Output("year-publication-chart", "figure"),
     Output("price-histogram", "figure"),
     Output("rating-chart", "figure")],
    [Input("price-slider", "value")]
)
def update_dashboard(max_price):
    df_books = df_top100_books[df_top100_books["book price"] <= max_price]
    
    # Criar a tabela filtrada
    table = html.Table([
        html.Thead(html.Tr([html.Th(col) for col in df_books.columns])),
        html.Tbody([
            html.Tr([html.Td(df_books.iloc[i][col]) for col in df_books.columns]) for i in range(min(len(df_books), 10))
        ])
    ])
    
    # Criar os gráficos
    fig_years = px.bar(df_books["year of publication"].value_counts().sort_index(), title="Books Published Per Year")
    fig_prices = px.histogram(df_books["book price"], title="Book Price Distribution")
    fig_ratings = px.bar(df_books["rating"].value_counts().sort_index(), title="Ratings Distribution")
    
    return table, fig_years, fig_prices, fig_ratings

# Executar a aplicação
if __name__ == "__main__":
    app.run_server(debug=True)
