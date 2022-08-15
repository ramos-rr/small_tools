import pytest

from libpythonpro.spam.db import Conexao


@pytest.fixture(scope='session')  # scope='module' ->  cria um objeto só durante o módulo de execução
def conexao():                   # scope='session' -> cria um objeto só para ser utilizado em toda a sessão (outside)
    # setup
    conexao_fixture = Conexao()  # A conexao vai gerenciar a autenticação do BD (login, senha)
    # yield == valor a ser injetado no teste
    yield conexao_fixture
    # tear_down
    conexao_fixture.fechar_conexao()


@pytest.fixture
def sessao(conexao):
    # setup
    sessao_fixture = conexao.gerar_sessao()  # A sessão serve para realizar as operações desejadas no BD
    # yield == valor a ser injetado no teste
    yield sessao_fixture
    # tear_down
    sessao_fixture.roll_back()
    sessao_fixture.fechar_sessao()
