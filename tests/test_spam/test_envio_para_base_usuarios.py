import pytest

from libpythonpro.spam.enviadador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.parametros_de_envio = None
        self.qte_emails_enviados = 0

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario.email, assunto, corpo)
        self.qte_emails_enviados += 1


@pytest.mark.parametrize(
    'usuarios', [
        [Usuario(nome='Renzo', email='ramos-rr@outlook.com')],
        [Usuario(nome='Renzo', email='ramos-rr@outlook.com'), Usuario(nome='Luciano', email='foo@baar.com.br')]
    ])
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        remetente='ramos-rr@outlook.com',
        assunto='Curso PythonPro',
        corpo='Confira os módulos Online'
    )
    assert len(usuarios) == enviador.qte_emails_enviados


def test_parametros_de_spam(sessao):
    sessao.salvar(Usuario(nome='Renzo', email='renzo@outlook.com.br'))
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        remetente='ramos-rr@outlook.com',
        assunto='Curso PythonPro',
        corpo='Confira os módulos Online'
    )
    assert enviador.parametros_de_envio == (
        'ramos-rr@outlook.com',
        'renzo@outlook.com.br',
        'Curso PythonPro',
        'Confira os módulos Online'
    )
