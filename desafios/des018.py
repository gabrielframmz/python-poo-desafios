from rich import print as rprint
from rich.panel import Panel

class Resenha:
    def __init__(self, n_membros, consumo_por_m, custo_kg, evento='Resenha'):
        self.n_membros = n_membros
        self.consumo_por_m = consumo_por_m
        self.custo_kg = custo_kg
        self.evento = evento

    def __str__(self):
        return self.evento

    def analysis(self):
        total_kg = (self.consumo_por_m * self.n_membros) / 1000
        total_custo = total_kg * self.custo_kg
        total_por_m = total_custo / self.n_membros
        conclusion = (f'[purple]{self.evento}[/] terá [purple]{self.n_membros}[/] participantes. '
                      f'Cada pessoa consumirá [purple]{self.consumo_por_m}g[/] '
                      f'com o custo de R$[purple]{self.custo_kg}[/]/kg. '
                      f'Total a comprar: [purple]{total_kg}kg[/], custo de R$[purple]{total_custo:,.2f}[/]. '
                      f'Cada pessoa pagará R$[purple]{total_por_m:,.2f}[/].')
        return conclusion


domingo = Resenha(12, 450, 54.69)
print(domingo.__doc__)
domingo.evento = 'Pescaria no Mato'
rprint(Panel(
    domingo.analysis(),
    title=domingo.__str__()
))
