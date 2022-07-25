'''
Módulo para a verificação de CPF
1. Considera apenas os números, ignorando os pontos e traços
2. Realiza a contagem de caracteres e retorna Falso se não contiver 11 números
3. Realiza a verificação do dígito, retornando Falso caso esteja errado.
4. Retorna verdadeiro se o CPF for digitado corretamente.

    >>> cpf = "325.171.828-25"
    True
    >>> cpf = 32517182826
    False
'''


def verifique_cpf(cpf) -> bool:
    cpf = str(cpf)
    cpf_list = [n for n in cpf if n in '0123456789']
    if len(cpf_list) != 11:
        return False
    else:
        somador = 10
        soma = 0
        for a in range(0, 9):
            soma += (int(cpf_list[a])*somador)
            somador -= 1
        divisor, resto = divmod(soma, 11)
        digito_um = 11 - resto
        if digito_um > 9:
            digito_um = 0
        if digito_um != int(cpf_list[-2]):
            return False
        else:
            somador = 11
            soma = 0
            for a in range(0, 10):
                soma += (int(cpf_list[a])*somador)
                somador -= 1
            divisor, resto = divmod(soma, 11)
            digito_dois = 11 - resto
            if digito_dois > 9:
                digito_dois = 0
            if digito_dois != int(cpf_list[-1]):
                return False
    return True


if __name__ == '__main__':
    cpf = verifique_cpf(input('digite o cpf: '))
    if not cpf:
        print('CPF inválido')