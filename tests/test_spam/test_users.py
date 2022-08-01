import pytest

from libpythonpro.spam.db import Conexao
from libpythonpro.spam.models import Usuario


@pytest.fixture
def conexao():
    # Setup
    conexao_obj = Conexao()
    # yeild retorna o valor que sejá injetado nos testes
    yield conexao_obj
    # Tear Down
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()


def test_salve_user(sessao):
    usuario = Usuario(nome='Renzo')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_list_user(sessao):
    usuarios = [Usuario(nome='Rafael'), Usuario(nome='Luciano')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
