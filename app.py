import requests
from bs4 import BeautifulSoup
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import csv

# Charger les données depuis le fichier CSV
df = pd.read_csv('tunisia_indicators.csv')

# Initialiser l'application Dash
app = dash.Dash(__name__)

# Définir la mise en page de l'application
app.layout = html.Div([
    html.H1("Tableau de Bord des Indicateurs de la Tunisie"),
    dcc.Dropdown(
        id='indicator-dropdown',
        options=[{'label': name, 'value': name} for name in df.columns[1:]],
        value=df.columns[1],  # Sélectionne le premier indicateur par défaut
        clearable=False
    ),
    dcc.Graph(id='indicator-graph'),
    html.P("Source des données : Banque Mondiale")
])

# Définir les callbacks pour mettre à jour le graphique en fonction de l'indicateur sélectionné
@app.callback(
    Output('indicator-graph', 'figure'),
    [Input('indicator-dropdown', 'value')]
)
def update_graph(selected_indicator):
    fig = px.line(df, x='Année', y=selected_indicator, title=selected_indicator)
    fig.update_layout(
        annotations=[
            dict(
                xref='paper', yref='paper', x=0, y=-0.2,
                showarrow=False, text="Source des données : Banque Mondiale"
            )
        ]
    )
    return fig

# Exécuter l'application
if __name__ == '__main__':
    app.run_server(debug=True)
