# small_tools
Repository composed by some small Python tools to validade strings, values and others so as to facilitate the coding process

Leia-me, isto é importante!


1. SUPORTADA A VERSÃO 3 DE PYTHON<br>
1.1. Instalado o Virtualenv<br><br>
2. ATENTO AOS REQUIREMENTS:<br>
2.1. para instalar através do terminal: "(.venv) pip install -r requirements-dev.txt"
<br><br>
3. DEFINIDO PEP-8 no flake8:<br>
3.1. Criar arquivo ".flake8"<br>
'''
[flake8]<br>
max-line-length=120<br>
exclude=.venv<br>
'''<br>
3.2. Rodar o teste no terminal: ".venv) flake8"<br><br>

4. ESTABELECIDO O SETUP.PY<br>
4.1. Para a realização do teste do setup.py, foi criado um VENV na pasta principal do PycharmProjects.<br>
4.1.1. Utilize o comando "<.venv>pip install -e small_tools" que ele já vai localizar o setup.py



TOPICOS A SEREM ABORDADOS:
1. GIT
2. VIRTUALENV
3. PIP
4. Atento ao pull request
5. Trabalhando com o ".gitignore"
5.1. Adicionado "rascunho" no ".gitignore"
6. Realizar alguns PULLREQUEST e testá-los
7. Obter uma reprova no PULLREQUEST <br>
7.1. cuidado com o comando no terminal 'git reset --hard HEAD^1', pode causar problemas<br>
7.2. Por isso, o jeito mais adequado de se fazer é através do
