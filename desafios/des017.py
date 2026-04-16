# etiqueta de venda de um produto
from rich.panel import Panel
from rich import print as rprint

class Produto:
    def __init__(self, nome, custo):
        self.nome = nome
        self.custo = custo

    def __str__(self):
        return self.nome

    def etiqueta(self):
        etiqueta = Panel(
            f'R${self.custo:,.2f}'.center(26, '.'),
            title=f'[blue]{self.nome}[/]',
            width=30,
        )
        return etiqueta


p1 = Produto('Xiaomi', 800)
p2 = Produto('RTX 1050 Ti Super', 5000)

rprint(p1.etiqueta())
rprint(p2.etiqueta())
