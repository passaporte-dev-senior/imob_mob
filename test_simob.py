from simob import *

def test_propriedade_com_proprietario_jogador_paga_aluguel():
    jogador = Jogador(exigente)
    proprietario = Jogador(exigente)
    propriedade = Propriedade(100, 51)
    propriedade.proprietario = proprietario

    jogador.compra_ou_aluga(propriedade)

    assert jogador.saldo == 249
    assert proprietario.saldo == 351
    assert propriedade.proprietario == proprietario

def test_exigente_sem_saldo_nao_compra_propriedade_disponivel():
    jogador = Jogador(exigente)
    propriedade = Propriedade(400, 51)

    jogador.compra_ou_aluga(propriedade)

    assert jogador.saldo == SALDO_INICIAL
    assert not propriedade.proprietario

def test_exigente_com_saldo_mas_aluguel_inferior_a_50_nao_compra_propriedade_disponivel():
    jogador = Jogador(exigente)
    propriedade = Propriedade(100, 40)

    jogador.compra_ou_aluga(propriedade)

    assert jogador.saldo == SALDO_INICIAL
    assert not propriedade.proprietario


def test_exigente_com_saldo_compra_propriedade_disponivel():
    jogador = Jogador(exigente)
    propriedade = Propriedade(100, 51)

    jogador.compra_ou_aluga(propriedade)

    assert jogador.saldo == 200
    assert propriedade.proprietario == jogador

def test_aleatorio_sorteado_true_sem_saldo_nao_compra_propriedade_disponivel():
    random.seed(42)

    jogador = Jogador(aleatorio)
    propriedade = Propriedade(400, 51)

    jogador.compra_ou_aluga(propriedade)

    assert jogador.saldo == SALDO_INICIAL
    assert not propriedade.proprietario

    random.seed()

def test_aleatorio_sorteado_false_com_saldo_nao_compra_propriedade_disponivel():
    random.seed(0)

    jogador = Jogador(aleatorio)
    propriedade = Propriedade(100, 51)

    jogador.compra_ou_aluga(propriedade)

    assert jogador.saldo == SALDO_INICIAL
    assert not propriedade.proprietario

    random.seed()

def test_aleatorio_sorteado_true_com_saldo_compra_propriedade_disponivel():
    random.seed(42)

    jogador = Jogador(aleatorio)
    propriedade = Propriedade(100, 51)

    jogador.compra_ou_aluga(propriedade)

    assert jogador.saldo == 200
    assert propriedade.proprietario == jogador

    random.seed()

def test_cauteloso_com_saldo_restante_igual_a_80_compra_propriedade_disponivel():
    jogador = Jogador(cauteloso)
    propriedade = Propriedade(220, 51)

    jogador.compra_ou_aluga(propriedade)

    assert jogador.saldo == 80
    assert propriedade.proprietario == jogador

def test_cauteloso_com_saldo_restante_maior_que_80_compra_propriedade_disponivel():
    jogador = Jogador(cauteloso)
    propriedade = Propriedade(210, 51)

    jogador.compra_ou_aluga(propriedade)

    assert jogador.saldo == 90
    assert propriedade.proprietario == jogador

def test_cauteloso_com_saldo_restante_menor_que_80_nao_compra_propriedade_disponivel():
    jogador = Jogador(cauteloso)
    propriedade = Propriedade(230, 51)

    jogador.compra_ou_aluga(propriedade)

    assert jogador.saldo == SALDO_INICIAL
    assert not propriedade.proprietario

def test_impulsivo_com_saldo_compra_propriedade_disponivel():
    jogador = Jogador(impulsivo)
    propriedade = Propriedade(150, 51)

    jogador.compra_ou_aluga(propriedade)

    assert jogador.saldo == 150
    assert propriedade.proprietario == jogador

def test_impulsivo_com_saldo_igual_preco_compra_propriedade_disponivel():
    jogador = Jogador(impulsivo)
    propriedade = Propriedade(300, 51)

    jogador.compra_ou_aluga(propriedade)

    assert jogador.saldo == 0
    assert propriedade.proprietario == jogador

def test_impulsivo_sem_saldo_nao_compra_propriedade_disponivel():
    jogador = Jogador(impulsivo)
    propriedade = Propriedade(301, 51)

    jogador.compra_ou_aluga(propriedade)

    assert jogador.saldo == SALDO_INICIAL
    assert not propriedade.proprietario

def test_libera_propriedades():
    jogador = Jogador(impulsivo)
    propriedade = Propriedade()

    propriedade.proprietario = jogador
    jogador.propriedades = [propriedade]

    libera_propriedades(jogador)

    assert not propriedade.proprietario
    assert not jogador.propriedades
