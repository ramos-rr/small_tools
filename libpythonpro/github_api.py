import requests


def buscar_avatar(usuario):
    """
    Busca o avatar de um usuário no GitHub

    :param usuario: str com nome do usuário no GitHub
    :return: str com o link do avatr
    """
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


# if __name__ == '__main__':
#     print(buscar_avatar('ramos-rr'))
