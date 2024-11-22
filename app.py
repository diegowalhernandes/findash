import dash
import dash_bootstrap_components as dbc
from dash import html
from cards import InvestmentCards
from resumo_geral import ResumoGeral

# Dados para o Resumo Geral
data_resumo = {
    "saldo_liquido": 5000.00,
    "saldo_bruto": 7000.00,
    "saldo_total": 12000.00,
    "lucro_bruto": 8000.00,
    "prejuizo_bruto": 3000.00,
    "fator_lucro": 2.67,
    "total_trades": 150,
    "media_lucros": 200.00,
    "media_prejuizos": 50.00,
    "razao_media": 4.00,
    "max_lucros": 1200.00,
    "max_prejuizos": 500.00
}

# Instâncias dos componentes
investment_cards = InvestmentCards()
resumo_geral = ResumoGeral(data_resumo)

# Inicialização do aplicativo Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout do aplicativo
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(resumo_geral.render(), width=4),  # Resumo Geral ocupa 4 colunas
        dbc.Col(
            dbc.Row([
                dbc.Col(card, width=6) for card in investment_cards.generate_cards()
            ]),
            width=8  # Os cards ocupam 8 colunas
        )
    ], justify="center", className="mt-4"),
], fluid=True)

if __name__ == "__main__":
    app.run_server(debug=True)
