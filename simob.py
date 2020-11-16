import random

SALDO_INICIAL = 300
LIMITE_DE_RODADAS = 1000

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

class Jogadores():
    def __init__(self, *jogadores):
        self.jogadores = jogadores
        self._da_vez = 0
        self.rodada = 1
        self.limite_de_rodadas = LIMITE_DE_RODADAS

    def vencedor(self):
        return max(self.jogadores)
    
    def jogando(self):
        return list(filter(bool, self.jogadores))
    
    def __contains__(self, item):
        return item in self.jogando()
    
    def __iter__(self):
        return self

    def __next__(self):
        if len(self.jogando()) == 1:
            raise StopIteration

        if self._da_vez >= len(self.jogando()):
            self._da_vez = 0
            self.rodada += 1

        if self.rodada > self.limite_de_rodadas:
            raise StopIteration
        
        jogador = self.jogando()[self._da_vez]
        self._da_vez += 1
        return jogador

def libera_propriedades(jogador):
    for p in jogador.propriedades:
        if p.proprietario == jogador:
            p.proprietario = None
    jogador.propriedades = []
