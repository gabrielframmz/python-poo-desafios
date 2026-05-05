# classe de um funcionário
from rich import print  # substitui o print built-in do python

class Funcionario:
    # atributos da classe
    empresa = 'Curso em Vídeo'

    def __init__(self, nome, setor, cargo):
        # atributos de instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def __str__(self):
        return self.nome

    def apresentar(self) -> str:
        return f'Olá :hand:, meu nome é [red]{self.nome}[/] e trabalho na {self.__class__.empresa} no setor {self.setor} como {self.cargo}.'


c1 = Funcionario('Gabriel', 'TI', 'Cooler de CPU')
print(c1)
print(c1.apresentar())
