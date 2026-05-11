# Polígonos
from abc import ABC, abstractmethod
from math import pi


class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self) -> float:
        # deve calcular o perímetro de cada polígono especificamente
        pass

    @abstractmethod
    def area(self) -> float:
        # deve calcular a área de cada polígono especificamente
        pass


class Quadrado(Poligono):
    def __init__(self, lado):
        super().__init__(qtd_lados = 4)
        self.lado = lado

    def perimetro(self):
        return self.lado * self.qtd_lados

    def area(self):
        return self.lado ** 2


class Circulo(Poligono):
    def __init__(self, raio):
        super().__init__(qtd_lados = 0)
        self.raio = raio

    def perimetro(self):
        return 2 * pi * self.raio

    def area(self):
        return pi * self.raio**2


###
q =Quadrado(5)
print(q, q.perimetro(), q.area())
c = Circulo(4)
print(c, c.perimetro(), c.area())
