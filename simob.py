import random

SALDO_INICIAL = 300

class Propriedade:
    def __init__(self, preco=300, aluguel=100):
        self.preco = preco
        self.aluguel = aluguel
        self.proprietario = None

def impulsivo(jogador, propriedade):
    return jogador.saldo >= propriedade.preco and not propriedade.proprietario

def exigente(jogador, propriedade):
    return impulsivo(jogador, propriedade) and propriedade.aluguel > 50

def cauteloso(jogador, propriedade):
    return impulsivo(jogador, propriedade) and (jogador.saldo - propriedade.preco) >= 80

def aleatorio(jogador, propriedade):
    return impulsivo(jogador, propriedade) and random.choice([True, False])

class Jogador:
    def __init__(self, estrategia, saldo=SALDO_INICIAL):
        self._saldo = saldo
        self.estrategia = estrategia

    @property
    def saldo(self):
        return self._saldo

    def __gt__(self, other):
        return self.saldo > other.saldo

    def __bool__(self):
        return self.saldo >= 0

    def paga(self, valor):
        self._saldo -= valor
        return valor

    def recebe(self, valor):
        self._saldo += valor

    def compra_ou_aluga(self, propriedade):
        if self.estrategia(self, propriedade):
            self.paga(propriedade.preco)
            propriedade.proprietario = self

        elif propriedade.proprietario:
            self.paga(propriedade.aluguel)
            if self.saldo >= 0:
                propriedade.proprietario.recebe(propriedade.aluguel)

class Jogadores(list):
    def __init__(self, *jogadores):
        super().__init__(jogadores)
        self.current = 0

    def vencedor(self):
        return max(self)
    
    def __contains__(self, item):
        return item in filter(lambda x: x, self)

    def __next__(self):
        if self.current >= len(self):
            self.current = 0
        
        j = self[self.current]
        self.current += 1
        return j

def libera_propriedades(jogador):
    for p in jogador.propriedades:
        if p.proprietario == jogador:
            p.proprietario = None
    jogador.propriedades = []
