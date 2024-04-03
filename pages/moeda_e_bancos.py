import dash
from dash import register_page, html



register_page(__name__, path="/moeda_e_bancos", title="Moedas e Bancos")

layout = html.Div("Moedas e Bancos")