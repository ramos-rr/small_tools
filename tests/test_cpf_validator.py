import pytest

from cpf_validator import verifique_cpf


@pytest.mark.parametrize(
    'lista_cpf_certo',
    [32517182825, '325.171.828-25', 38525944807, '38525944807']
)
def test_right_cpf(lista_cpf_certo):
    cpf = verifique_cpf(lista_cpf_certo)
    assert int(cpf)


@pytest.mark.parametrize(
    'lista_cpf_errado',
    [32187981164, '321892+1647+', 78913298921]
)
def test_wrong_cpf(lista_cpf_errado):
    cpf = verifique_cpf(lista_cpf_errado)
    assert not cpf
