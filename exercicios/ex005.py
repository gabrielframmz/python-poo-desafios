# abstração em python
from abc import ABC, abstractmethod

class Abstrata(ABC):    # ABC define que esta classe não pode instanciar objetos. Atua apenas como super classe
    def __init__(self):
        self.exemplo = 'teste de abstração...'

    def m_concreto(self):
        print('método concreto.')

    @abstractmethod
    def m_abstrato(self):
        return 'Deve OBRIGATÓRIAMENTE ser definido na classe filha.'


class Especializada(Abstrata):
    def __init__(self):
        super().__init__()
        self.exemplo += f' Pai: <{Abstrata.__name__}>'
        self.desc = f'{self.__class__} esta classe é específica!'

    def m_abstrato(self):
        print(f'{super().m_abstrato()} - método abstrato.')


###
teste00 = Especializada()
print(teste00.exemplo)
print(teste00.desc)
teste00.m_concreto()
teste00.m_abstrato()
