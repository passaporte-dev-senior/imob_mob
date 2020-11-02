from simob import *
import pytest

def test_um_vencedor_na_lista_de_jogadores():
    jogador01 = Jogador(impulsivo)
    jogador02 = Jogador(impulsivo)
    jogadores = Jogadores(jogador01, jogador02)

    jogador01.paga(301)

    assert jogadores.vencedor() == jogador02 
    assert jogador02 in jogadores
    assert not jogador01 in jogadores
    assert not Jogador(impulsivo) in jogadores


def test_vencedor_lista_de_jogadores_maior_saldo():
    jogador01 = Jogador(impulsivo, saldo=1000)
    jogador02 = Jogador(impulsivo, saldo=100)
    jogadores = Jogadores(jogador01, jogador02)
    
    assert jogadores.vencedor() == jogador01

def test_vencedor_lista_de_jogadores_maior_saldo():
    jogador01 = Jogador(impulsivo, saldo=100)
    jogador02 = Jogador(impulsivo, saldo=200)
    jogador03 = Jogador(impulsivo, saldo=200)
    jogadores = Jogadores(jogador01, jogador02, jogador03)
    
    assert jogadores.vencedor() == jogador02

def test_next_lista_de_jogadores_retorna_ao_inicio():
    jogador01 = Jogador(impulsivo, saldo=1000)
    jogador02 = Jogador(impulsivo, saldo=100)
    jogadores = Jogadores(jogador01, jogador02)

    assert next(jogadores) == jogador01
    assert next(jogadores) == jogador02
    assert next(jogadores) == jogador01

def test_next_pula_jogador_com_saldo_negativo():
    jogador01 = Jogador(impulsivo, saldo=1000)
    jogador02 = Jogador(impulsivo, saldo=100)
    jogador03 = Jogador(impulsivo, saldo=101)
    jogadores = Jogadores(jogador01, jogador02, jogador03)

    assert next(jogadores) == jogador01
    assert next(jogadores) == jogador02
    assert next(jogadores) == jogador03
    assert next(jogadores) == jogador01
    assert jogadores.rodadas == 2

    jogador02.paga(200)

    assert next(jogadores) == jogador03
    assert next(jogadores) == jogador01

def test_next_lanca_stop_iteration_quando_resta_apenas_um_jogador():
    jogador01 = Jogador(impulsivo, saldo=1000)
    jogador02 = Jogador(impulsivo, saldo=100)
    jogadores = Jogadores(jogador01, jogador02)

    assert next(jogadores) == jogador01
    assert next(jogadores) == jogador02
    assert next(jogadores) == jogador01

    jogador02.paga(200)

    with pytest.raises(StopIteration):
        next(jogadores) == jogador01

    assert jogadores.vencedor() == jogador01

def test_next_lanca_stop_iteration_quando_alcanca_limite_de_rodadas():
    jogador01 = Jogador(impulsivo, saldo=100)
    jogador02 = Jogador(impulsivo, saldo=1000)
    jogadores = Jogadores(jogador01, jogador02)

    jogadores.limite_de_rodadas = 3

    assert next(jogadores) == jogador01
    assert next(jogadores) == jogador02
    assert next(jogadores) == jogador01
    assert next(jogadores) == jogador02
    assert next(jogadores) == jogador01
    assert next(jogadores) == jogador02

    with pytest.raises(StopIteration):
        next(jogadores) == jogador01

    assert jogadores.vencedor() == jogador02
