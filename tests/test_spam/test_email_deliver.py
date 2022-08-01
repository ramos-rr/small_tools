import pytest

from libpythonpro.spam.email_deliver import Enviador, EmailInvalido


def test_crate_email_deliver():
    enviador = Enviador()
    assert enviador is not None


def test_remetente():
    enviador = Enviador()
    destinatarios = ['foo@bar.com.br', 'ramos-rr@outlook.com', 'felipao@ig.com.br']
    for destinatario in destinatarios:
        resultado = enviador.enviar(
            rementente='rafaelblk182@gmail.com',
            destinatario=destinatario,
            assunto='Cursos Python Pro',
            corpo='Primeira turma Guido Von Rossum Aberto'
        )
        assert destinatario in resultado


@pytest.mark.parametrize(
    'destinatario',
    ['foo@bar.com.br', 'ramos-rr@outlook.com', 'felipao@ig.com.br']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        rementente='rafaelblk182@gmail.com',
        destinatario=destinatario,
        assunto='Cursos Python Pro',
        corpo='Primeira turma Guido Von Rossum Aberto'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente_invalido',
    ['foobar.com.br', '', 'a.com.br']
)
def test_remetente_invalido(remetente_invalido):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            rementente=remetente_invalido,
            destinatario='rafaelblk182@gmail.com',
            assunto='Cursos Python Pro',
            corpo='Primeira turma Guido Von Rossum Aberto'
        )
