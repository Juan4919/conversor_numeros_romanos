from main import romano_a_entero,RomanNumberError
import pytest

def test_romano_a_entero():
    assert romano_a_entero("I") == 1

def test_romano_a_entero_MDCCXIII():
    assert romano_a_entero("MDCCXIII") == 1713

def test_romano_a_entero_IV():
    assert romano_a_entero("IV") == 4    


def test_romano_a_entero_no_repetir_mas_de_tres():
    with pytest.raises(RomanNumberError ) as exeptionInfo:
        romano_a_entero("IIII")
    assert str(exeptionInfo.value) == "No se puede repetir el valor mas de tres veces"   