# Mantenha o seu cursor aqui quando não estiver pilotando: 

import random
import pytest
pytest.main([__file__, '-v', '-p', 'no:warnings'])

class Propriedade:
    def __init__(self, preco=300, aluguel=100, proprietario=False):
        self.preco = preco
        self.aluguel = aluguel
        self.proprietario = proprietario


class Jogador:
    def __init__(self, estrategia, saldo=300):
        self.saldo = saldo
        self.estrategia = estrategia

    def paga(self, valor):
        self.saldo -= valor

    def __bool__(self):
        return self.saldo >= 0

def test_saldo_jogador():
    jogador = Jogador(estrategia='impulsivo')
    jogador.paga(100)
    assert jogador
    assert jogador.saldo == 200

def test_jogador_eh_falso_quanto_tem_saldo_negativo():
    jogador = Jogador(estrategia='impulsivo', saldo=-100)
    assert not jogador


def devo_comprar(estrategia, saldo, propriedade):
    preco = propriedade.preco
    aluguel = propriedade.aluguel
    
    if propriedade.proprietario:
        return False
    if saldo < preco:
        return False
    if estrategia == 'impulsivo':
        return True
    if estrategia == 'cauteloso':
        return (saldo - preco) >= 80
    if estrategia == 'aleatorio':
        return random.choice([True, False])
    if estrategia == 'exigente':
        return aluguel > 50


def test_comprar_com_proprietario():
    assert devo_comprar('exigente', saldo=300, propriedade=Propriedade(100, 51, True)) == False

def test_exigente_sem_saldo():
    assert devo_comprar('exigente', saldo=0, propriedade=Propriedade(100, 51)) == False

def test_exigente_com_saldo_mas_aluguel_inferior_a_50():
    assert devo_comprar('exigente', saldo=300, propriedade=Propriedade(100, 40)) == False

def test_exigente_com_saldo():
    assert devo_comprar('exigente', saldo=300, propriedade=Propriedade(100, 51)) == True

def test_aleatorio_sem_saldo_true():
    random.seed(42)
    assert devo_comprar('aleatorio', saldo=0, propriedade=Propriedade(100)) == False

def test_aleatorio_com_saldo_false():
    random.seed(0)
    assert devo_comprar('aleatorio', saldo=300, propriedade=Propriedade(100)) == False

def test_aleatorio_com_saldo_true():
    random.seed(42)
    assert devo_comprar('aleatorio', saldo=300, propriedade=Propriedade(100)) == True

def test_cauteloso_com_saldo_restante_igual_a_80():
    assert devo_comprar(estrategia='cauteloso', saldo=300, propriedade=Propriedade(220)) == True

def test_cauteloso_com_saldo_restante_maior_que_80():
    assert devo_comprar(estrategia='cauteloso', saldo=300, propriedade=Propriedade(210)) == True

def test_cauteloso_com_saldo_restante_menor_que_80():
    assert devo_comprar(estrategia='cauteloso', saldo=300, propriedade=Propriedade(230)) == False

def test_impulsivo_com_saldo():
    assert devo_comprar(estrategia='impulsivo', saldo=300, propriedade=Propriedade(150)) == True

def test_impulsivo_com_saldo_igual_preco():
    assert devo_comprar(estrategia='impulsivo', saldo=150, propriedade=Propriedade(150)) == True

def test_impulsivo_sem_saldo():
    assert devo_comprar(estrategia='impulsivo', saldo=0, propriedade=Propriedade(150)) == False    


































# @pytest.mark.parametrize("params, expected", (
#     ((), True),
# ))
# def test_name(params, expected):
#     assert True
