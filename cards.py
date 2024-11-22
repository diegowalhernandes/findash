import dash_bootstrap_components as dbc
from dash import html

class InvestmentCards:
    def __init__(self):
        # Dados iniciais dos cards
        self.card_data = [
            {"title": "Traders", "value": "0", "id": "traders-card"},
            {"title": "Lucros", "value": "R$ 0,00", "id": "profits-card"},
            {"title": "Prejuízos", "value": "R$ 0,00", "id": "losses-card"},
            {"title": "Saldo", "value": "R$ 0,00", "id": "balance-card"}
        ]

    def create_card(self, title, value, card_id):
        """
        Método para criar um card individual.
        """
        return dbc.Card(
            dbc.CardBody([
                html.H5(title, className="card-title"),
                html.H2(value, className="card-value", id=card_id),
            ]),
            className="m-2"
        )

    def generate_cards(self):
        """
        Gera uma lista de cards usando os dados fornecidos.
        """
        return [
            self.create_card(card["title"], card["value"], card["id"])
            for card in self.card_data
        ]
