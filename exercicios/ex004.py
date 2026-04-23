# Herança em POO (exemplo simples)

class Personagem:
    def __init__(self, nome, level):
        self.nome = nome
        self.level = level

    def andar(self):
        print('Você andou!')


class Guerreiro(Personagem):
    def __init__(self, nome, level, armadura):
        super().__init__(nome, level)
        self.armadura = armadura

    def bloquear(self):
        print('Bloqueou os danos!')

class Ladino(Personagem):
    def __init__(self, nome, level, agilidade):
        super().__init__(nome, level)
        self.agilidade = agilidade

    def roubar(self):
        print('Levou vantagem!')

class Mago(Personagem):
    def __init__(self, nome, level, magia):
        super().__init__(nome, level)
        self.magia = magia

    def lançar_magia(self):
        print('Bola de fogo!')
