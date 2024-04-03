import dash
from dash import register_page, html



register_page(__name__, path="/contabilidade_nacional", title="Contabilidade Nacional")

layout = html.Div("Contabilidade Nacional")