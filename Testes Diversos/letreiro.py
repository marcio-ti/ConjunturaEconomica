import dash
from dash import dcc, html, Input, Output
import pandas as pd

# Suponha que você já tenha os dados das ações em um DataFrame (por exemplo, obtidos com a biblioteca B3Api)
# Aqui, usaremos dados fictícios para ilustração.
data = pd.DataFrame({
    'Ticker': ['ITSA4', 'BBDC4','AMER3'],
    'Price': [10.08, 23.44, 0.56]
})

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Interval(id='interval-component', interval=3000, n_intervals=0),  # Atualiza a cada 5 segundos
    html.H1("Preço das Ações da B3"),
    html.Div(id='stock-price')
])

@app.callback(Output('stock-price', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_stock_price(n):
    # Aqui, você pode buscar os dados reais da B3 usando a biblioteca B3Api ou outra fonte
    # Por enquanto, usaremos os dados fictícios
    stock_ticker = data.loc[n % len(data), 'Ticker']
    stock_price = data.loc[n % len(data), 'Price']
    return f"Preço de {stock_ticker}: R${stock_price:.2f}"

if __name__ == '__main__':
    app.run_server(debug=True)