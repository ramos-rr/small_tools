from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):  # teste para Salvar Usuário em um Bando de Dados
    usuario = Usuario(nome='Renzo', email='ramos-rr@outlook.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='Renzo', email='ramos-rr@outlook.com'), Usuario(nome='Luciano', email='foo@baar.com.br')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar_usuarios()
