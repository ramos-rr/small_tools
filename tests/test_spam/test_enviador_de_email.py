import pytest
from libpythonpro.spam.enviadador_de_email import Enviador, EmailInvalido


def test_criar_enviador_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['foo@bar.com',
    'ramos-rr@outlook.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente=remetente,
        destinatario='rafaelblk182@hotmail.com',
        assunto='Cursos PythonPro',
        corpo='Veja esta novidade agora em modo Online!'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['foobar.com',
    'ramos-rroutlook.com',
     '']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(expected_exception=EmailInvalido):
        enviador.enviar(
            remetente=remetente,
            destinatario='rafaelblk182@hotmail.com',
            assunto='Cursos PythonPro',
            corpo='Veja esta novidade agora em modo Online!'
        )
