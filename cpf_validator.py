def verifique_cpf(cpf) -> bool or int:
    """
    Função que retorna se o CPF digitado é válido. O usuário pode entrar com o CPF juntamente com os pontos e traços
    que pos função somente irá considerar os números:
    Ex:
    >>> verifique_cpf('325.171.828-25')
    32517182825
    >>> verifique_cpf('385259448-07')
    38525944807
    >>> verifique_cpf('32517182825')
    32517182825
    >>> verifique_cpf('32517182829')
    False

    :param cpf: Conjunto de caracteres numéricos que formam o CPF.
    :return: True se o CPF digitado for válido. False se o CPF digitado não for válido
    """
    cpf = str(cpf)
    cpf_list = [n for n in cpf if n in '0123456789']
    if len(cpf_list) != 11:
        return False
    else:
        somador = 10
        soma = 0
        for pos in range(0, 9):
            soma += (int(cpf_list[pos])*somador)
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
            for pos in range(0, 10):
                soma += (int(cpf_list[pos])*somador)
                somador -= 1
            divisor, resto = divmod(soma, 11)
            digito_dois = 11 - resto
            if digito_dois > 9:
                digito_dois = 0
            if digito_dois != int(cpf_list[-1]):
                return False
    cpf = ''.join(cpf_list)
    return int(cpf)


if __name__ == '__main__':
    cpf = verifique_cpf('786.605.138-00')
    print(cpf)