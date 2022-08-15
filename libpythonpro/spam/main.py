class EnviadorDeSpam:
    def __init__(self, sessao, enviador):
        self.enviador = enviador
        self.sessao = sessao

    def enviar_emails(self, remetente, assunto, corpo):
        for usuario in self.sessao.listar_usuarios():
            self.enviador.enviar(
                destinatario=usuario,
                remetente=remetente,
                assunto=assunto,
                corpo=corpo
            )
