# CANETA que escreve colorido?
from random import choice
from rich import print

class Caneta:
    cores = {
        'vermelha': 'red',
        'verde': 'green',
        'azul': 'blue'
    }

    def __init__(self, cor, destampada=False):
        self.cor = cor
        self.destampada = destampada

        if self.cor not in Caneta.cores.keys():
            print(f'"{self.cor}" não existe no sistema. Uma outra cor será escolhida aleatóriamente.')
            print('[underline]>>> DICA: ESCREVA AS CORES EM PORTUGUÊS E NO GENÊRO FEMININO.[/]')
            self.cor = choice([cor for cor in Caneta.cores.keys()])

    def __str__(self):
        return f'Você tem uma caneta da cor {self.cor.upper()} que está {"DESTAMPADA" if self.destampada else "TAMPADA"}.'

    def estado_tampa(self):
        self.destampada = not self.destampada

    def escrever(self, msg=''):
        if self.destampada:
            print(f'[{Caneta.cores[self.cor]}]{msg}[/]')
        else:
            print(f'A caneta está tampada! Por favor, remova a tampa.')
