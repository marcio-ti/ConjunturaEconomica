import dash
from dash import register_page, html



register_page(__name__, path="/", title="Dashboard")

layout = html.Div("Dashboard")