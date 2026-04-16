# simulação simplística de uma conta bancária

class ContaBanco:
    """
    Cria uma conta bancária e permite atualizar os atributos.

    self.idb            - número único da conta
    self.titular        - nome do indivíduo
    self.saldo          - fundos depositados (0)
    self.priv_saldo     - define se o saldo é privado (True)
    """
    def __init__(self, idb, titular, saldo = 0, priv_saldo = True):
        self.idb = idb
        self.titular = titular
        self.saldo = saldo
        self.priv_saldo = priv_saldo

    def __str__(self):
        if self.priv_saldo:
            return f'A conta {self.idb} pertence ao titular {self.titular}.\nO saldo é privado.'
        else:
            return f'A conta {self.idb} pertence ao titular {self.titular}.\nSaldo atual: R${self.saldo:,.2f}'

    def deposito(self, valor):
        self.saldo += valor
        return self

    def saque(self, valor):
        if self.saldo < valor:
            return 'A operação não pôde ser autorizada. SALDO INSUFICIENTE'
        else:
            self.saldo -= valor
            return self


## PROGRAMA PRINCIPAL
minha_conta = ContaBanco(1, 'gabrielgg', 50000, False)
print(minha_conta.__doc__)
print(minha_conta)
print(minha_conta.saque(2000))
print(minha_conta.deposito(900))
print(minha_conta.saque(100_000))

