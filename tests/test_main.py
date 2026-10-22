import pytest

from main import calcular_area_triangulo

def test_calcular_area_triangulo():
    #Resultado obtenido (real)
    actual_result = calcular_area_triangulo(13, 3)

    #assert (estamos verificando) que el actual_result 
    #es igual al resultado esperado (esperado)
    assert actual_result == pytest.approx(19.5, abs=0.01)