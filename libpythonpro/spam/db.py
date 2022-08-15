from typing import Type
from time import sleep
from libpythonpro.spam.modelos import Usuario


class Sessao:
    contador_de_sessao = 0
    lista_usuarios = []

    def salvar(self, usuario: Type[Usuario]) -> None:
        self.contador_de_sessao += 1
        usuario.id = self.contador_de_sessao
        self.lista_usuarios.append(usuario)

    def listar_usuarios(self) -> list:
        return self.lista_usuarios

    def roll_back(self):
        self.lista_usuarios.clear()  # Necessário chamar a função CLEAR para fucionar!

    def fechar_sessao(self):
        pass


class Conexao:

    def __init__(self):
        sleep(1)

    def gerar_sessao(self) -> Type[Sessao]:
        return Sessao()

    def fechar_conexao(self):
        pass
