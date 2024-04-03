import dash
import dash_bootstrap_components as dbc
from dash import Dash, html, Input, Output, State, callback, page_container
import dash.exceptions


app = Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP],
    use_pages=True,
    suppress_callback_exceptions=True,
)

app.layout = html.Div(
    children=[
        # ---------------------------------------------------------------------------------------------- #
        # Menu
        html.Div(
            id="menu",
            children=[
                # ---------------------------------------------------------------------------------------------- #
                # Dashboard
                dbc.Nav(
                    vertical="md",
                    pills=True,
                    children=[
                        dbc.NavLink(
                            href="/",
                            active="exact",
                            className="mb-2",
                            children=['Dashboard']
                        ),
                    ],
                ),
                
                
                # ---------------------------------------------------------------------------------------------- #
                # Moeda e Bancos
                dbc.Nav(
                    vertical="md",
                    pills=True,
                    children=[
                        dbc.NavLink(
                            href="/moeda_e_bancos",
                            active="exact",
                            className="mb-2",
                            children=['Moedas e Bancos']
                        ),
                    ],
                ),
                
                # ---------------------------------------------------------------------------------------------- #
                # Contabilidade Nacional
                dbc.Nav(
                    vertical="md",
                    pills=True,
                    children=[
                        dbc.NavLink(
                            href="/contabilidade_nacional",
                            active="exact",
                            className="mb-2",
                            children=['Contabilidade Nacional']
                        ),
                    ],
                ),
            ]
        ),
        
        # ---------------------------------------------------------------------------------------------- #
        # Página
        html.Div(id="pagina", children=[page_container]),
    ]
)

# SERVIDOR
if __name__ == "__main__":
    app.run(
        debug=True,
        port="8050",
        dev_tools_ui=True,
        dev_tools_hot_reload=True,
        threaded=True,
    )
    # app.run(
    #    host="0.0.0.0",
    #    port="8080",
    #    threaded=True,
    # )
