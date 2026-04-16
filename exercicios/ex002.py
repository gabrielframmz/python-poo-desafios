# exemplo de criação de uma classe

class Gafanhoto():
    def __init__(self, nome = 'Pessoa', idade = 18):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'{self.nome}'

    def aniversario(self):
        self.idade += 1


### testes
g1 = Gafanhoto('Gabriel', 19)
g1.aniversario()
print(g1)
print(g1.__dict__)
