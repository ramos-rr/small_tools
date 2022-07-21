# método tradicional com lista auxiliar:
lista = []
for i in range(10):
    lista.append(i)
print(lista)


# método de list compreehention
lista2 = [j for j in range(10)]
print(lista2)


# método de descobrir posição por NEXT atraves de tipo LIST COMPREEHENTION
# lista inicialmente já existente
lista_numeros = [4, 12, 26, 33, 49, 55, 60, 78, 81, 97]
print(lista_numeros)
# Número que serve como base
numero_referencia = 100
try:
    # função para descobrir a POSIÇÃO NA LISTA quando o número_refência encontra o primeiro valor maior que si
    local = next(_ for _, val in enumerate(lista_numeros) if val > numero_referencia)
except StopIteration:
    # caso o valor não seja encontrado, é porque a lista acabou. Assim, evita-se a exceção de StopIteration
    local = len(lista_numeros)
try:
    # função para descobrir o PRIMEIRO ELEMENTO NA LISTA de número_refência com valor maior que si
    elemento = next(y for y in lista_numeros if y > numero_referencia)
except StopIteration:
    # caso o valor não seja encontrado, é porque a lista acabou. Assim, evita-se a exceção de StopIteration
    elemento = ''
print(f'O número {numero_referencia} deve entrar na posição {local} da lista')
print(f'O número {numero_referencia} é superado pelo {elemento} da lista' if elemento != '' else
      f'O número {numero_referencia} não é superado por nenhum elemento na lista e será o maior')
print(lista_numeros)
