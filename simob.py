# Mantenha o seu cursor aqui quando não estiver pilotando: 

import random
# import pytest
# pytest.main([__file__, '-v', '-p', 'no:warnings'])

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
        else:
            self.saldo -= propriedade.aluguel

#     def paga(self, valor):
#         self.saldo -= valor

#     def __bool__(self):
#         return self.saldo >= 0

# def test_saldo_jogador():
#     jogador = Jogador(estrategia='impulsivo')
#     jogador.paga(100)
#     assert jogador
#     assert jogador.saldo == 200

# def test_jogador_eh_falso_quanto_tem_saldo_negativo():
#     jogador = Jogador(estrategia='impulsivo', saldo=-100)
#     assert not jogador
