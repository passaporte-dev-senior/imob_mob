import random

SALDO_INICIAL = 300
LIMITE_DE_RODADAS = 1000

class Propriedade:
    def __init__(self, preco=300, aluguel=100):
        self.preco = preco
        self.aluguel = aluguel
        self.proprietario = None

    def tem_proprietario(self):
        return self.proprietario

    def cobra_aluguel(self, jogador):
        aluguel = jogador.paga(self.aluguel)
        if jogador:
            self.proprietario.recebe(aluguel)
        else:
            self.despeja(jogador)

    def se_vende(self, jogador):
        jogador.paga(self.preco)
        self.proprietario = jogador
        jogador.propriedades.append(self)

    def despeja(self, jogador):
        for propriedade in jogador.propriedades:
            propriedade.proprietario = None
        jogador.propriedades = []


def impulsivo(jogador, propriedade):
    return True

def exigente(jogador, propriedade):
    return propriedade.aluguel > 50

def cauteloso(jogador, propriedade):
    return jogador.saldo - propriedade.preco >= 80

def aleatorio(jogador, propriedade):
    return random.choice([True, False])

class Jogador:
    def __init__(self, estrategia, saldo=SALDO_INICIAL):
        self._saldo = saldo
        self.estrategia = estrategia
        self.propriedades = []

    @property
    def saldo(self):
        return self._saldo

    def __gt__(self, other):
        return self.saldo > other.saldo

    def __bool__(self):
        return self.saldo >= 0

    def __str__(self):
        return f'Jogador({self.estrategia.__name__}, saldo={self.saldo})'

    def paga(self, valor):
        self._saldo -= valor
        return valor

    def recebe(self, valor):
        self._saldo += valor

    def compra_ou_aluga(self, propriedade):
        if propriedade.tem_proprietario():
            propriedade.cobra_aluguel(self)

        elif self.saldo >= propriedade.preco and self.estrategia(self, propriedade):
            propriedade.se_vende(self)


class Jogadores(list):
    def __init__(self, *jogadores):
        super().__init__(jogadores)

    def embaralha(self):
        random.shuffle(self)
        return self

    def vencedor(self):
        return max(self)

    @property
    def jogando(self):
        return list(filter(bool, self))

    def resta_um_jogador(self):
        return len(self.jogando) == 1

    def __contains__(self, item):
        return item in self.jogando

    # def incrementa_numero_de_rodadas(self):
    #     self.rodadas += 1
    #     if self.excedido_limite_de_rodadas():
    #         raise StopIteration

    # def excedido_limite_de_rodadas(self):
    #     return self.rodadas > self.limite_de_rodadas
    
    # def __next__(self):
    #     if self.resta_um_jogador():
    #         raise StopIteration

    #     if self._da_vez >= len(self.jogando):
    #         self.incrementa_numero_de_rodadas()
    #         self._da_vez = 0

    #     jogador = self.jogando[self._da_vez]
    #     self._da_vez += 1
    #     return jogador

# def libera_propriedades(jogador):
#     for p in jogador.propriedades:
#         p.proprietario = None
#     jogador.propriedades = []

'''

class Jogadores:
    def __init__(self, *jogadores):
        self.jogadores = jogadores
        self._da_vez = 0
        self.rodadas = 1
        self.limite_de_rodadas = LIMITE_DE_RODADAS

    def vencedor(self):
        return max(self.jogadores)

    @property
    def jogando(self):
        return list(filter(bool, self.jogadores))

    def resta_um_jogador(self):
        return len(self.jogando) == 1

    def incrementa_numero_de_rodadas(self):
        self.rodadas += 1
        if self.excedido_limite_de_rodadas():
            raise StopIteration

    def excedido_limite_de_rodadas(self):
        return self.rodadas > self.limite_de_rodadas
    
    def __contains__(self, item):
        return item in self.jogando

    def __iter__(self):
        return JogadoresIterable(self)

class JogadoresIterable:
    def __init__(self, jogadores):
        self._jogadores = jogadores

    def __next__(self):
        if self._jogadores.resta_um_jogador():
            raise StopIteration

        if self._jogadores._da_vez >= len(self._jogadores.jogando):
            self._jogadores.incrementa_numero_de_rodadas()
            self._jogadores._da_vez = 0

        jogador = self._jogadores.jogando[self._jogadores._da_vez]
        self._jogadores._da_vez += 1
        return jogador

'''