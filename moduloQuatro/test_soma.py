import pytest
from soma import soma
from parametros import *

@pytest.mark.parametrize(variaveis_soma, parametros_soma)
def test_soma(a,b,esperado):
    assert soma(a,b) == esperado