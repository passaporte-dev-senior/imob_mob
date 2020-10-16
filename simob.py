import random

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
    def __init__(self, estrategia, saldo=300):
        self.saldo = saldo
        self.estrategia = estrategia

    def paga(self, propriedade):
        if self.estrategia(self, propriedade):
            self.saldo -= propriedade.preco
            propriedade.proprietario = self
        elif propriedade.proprietario:
            self.saldo -= propriedade.aluguel
            propriedade.proprietario.saldo += propriedade.aluguel
