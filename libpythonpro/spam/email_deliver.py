class Enviador:
    def enviar(self, destinatario, rementente, assunto, corpo):
        if '@' not in rementente:
            raise EmailInvalido(f'Email inválido: {rementente}')
        return destinatario


class EmailInvalido(Exception):
    pass
