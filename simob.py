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

    def __gt__(self, other):
        return self.saldo > other.saldo

    def __bool__(self):
        return self.saldo >= 0

    def paga(self, propriedade):
        if self.estrategia(self, propriedade):
            self.saldo -= propriedade.preco
            propriedade.proprietario = self
        elif propriedade.proprietario:
            self.saldo -= propriedade.aluguel
            if self.saldo >= 0:
                propriedade.proprietario.saldo += propriedade.aluguel

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
