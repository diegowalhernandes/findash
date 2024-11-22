import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.express as px

class ResumoGeral:
    def __init__(self, data):
        """
        Inicializa o componente Resumo Geral com dados fornecidos.
        :param data: Dicionário contendo os dados para o gráfico e a lista.
        """
        self.data = data

    def create_pie_chart(self):
        """
        Cria o gráfico de pizza com os dados fornecidos.
        """
        pie_data = {
            "Categoria": ["Saldo Líquido", "Lucro Bruto", "Prejuízo Bruto"],
            "Valores": [
                self.data["saldo_liquido"],
                self.data["lucro_bruto"],
                self.data["prejuizo_bruto"]
            ]
        }
        fig = px.pie(pie_data, values="Valores", names="Categoria", title="Resumo Geral")
        return dcc.Graph(figure=fig)

    def create_list(self):
        """
        Cria a lista com os dados fornecidos.
        """
        return html.Ul(
            children=[
                html.Li(f"Saldo Líquido: R$ {self.data['saldo_liquido']:.2f}"),
                html.Li(f"Saldo Bruto: R$ {self.data['saldo_bruto']:.2f}"),
                html.Li(f"Saldo Total: R$ {self.data['saldo_total']:.2f}"),
                html.Li(f"Lucro Bruto: R$ {self.data['lucro_bruto']:.2f}"),
                html.Li(f"Prejuízo Bruto: R$ {self.data['prejuizo_bruto']:.2f}"),
                html.Li(f"Fator Lucro: {self.data['fator_lucro']:.2f}"),
                html.Li(f"Total Trades: {self.data['total_trades']}"),
                html.Li(f"Média Lucros: R$ {self.data['media_lucros']:.2f}"),
                html.Li(f"Média Prejuízos: R$ {self.data['media_prejuizos']:.2f}"),
                html.Li(f"Razão Média: {self.data['razao_media']:.2f}"),
                html.Li(f"Máximo Lucros: R$ {self.data['max_lucros']:.2f}"),
                html.Li(f"Máximo Prejuízos: R$ {self.data['max_prejuizos']:.2f}")
            ],
            className="mt-3"
        )

    def render(self):
        """
        Renderiza o componente completo.
        """
        return dbc.Container([
            self.create_pie_chart(),
            self.create_list()
        ], className="mt-4")
