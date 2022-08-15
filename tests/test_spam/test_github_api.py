from pytest_mock import mocker

from libpythonpro import github_api
from unittest.mock import Mock

# Realização de teste deta natureza com a utilização da Lib MOCK, para evitar fazer muitas chamadas no servidor
# Para tanto, vamos criar um mock de um site, que retorna um json em forma de dicionário
# Já para se desfazer do MOCK, utilizamos a LIB PYTEST-MOCK para devolver os métodos ao original para que o primeiro
# teste não interfira no segundo


def test_avatar_url_com_mock():
    # 1. Criar um Mock()
    resp_mock = Mock()
    # 2. Transformar url em variável
    avatar_url_manual = 'https://avatars.githubusercontent.com/u/107194089?v=4'
    # 3. definir qual o valor que vai ser respondido
    resp_mock.json.return_value = {'avatar_url': avatar_url_manual}
    # 4. para não influenciar no teste abaixo, devemos extrair a chamada original e após o teste, deve-se redefinir
    get_original = github_api.requests.get
    # 5. Aqui, sobrescrevemos o chamado do requests para receber o valor definido mais acima
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('ramos-rr')
    github_api.requests.get = get_original
    assert url == 'https://avatars.githubusercontent.com/u/107194089?v=4'


def test_avatar_url_com_mocker(mocker):
    # 1. Criar um Mock()
    resp_mock = Mock()
    # 2. Transformar url em variável
    avatar_url_manual = 'https://avatars.githubusercontent.com/u/107194089?v=4'
    # 3. Definir qual o valor que vai ser respondido
    resp_mock.json.return_value = {'avatar_url': avatar_url_manual}
    # 4. Criar uma variável para o mocker sobrescrever a biblioteca que será simulada
    get_mock = mocker.patch('libpythonpro.github_api.requests.get')
    # 5. Definir o valor a ser obtido como resposta. Após a utilização, o mocker retorna ao valor original.
    get_mock.return_value = resp_mock
    url = github_api.buscar_avatar('ramos-rr')
    assert url == 'https://avatars.githubusercontent.com/u/107194089?v=4'


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('renzo')
    assert 'https://avatars.githubusercontent.com/u/402714?v=4' == url
