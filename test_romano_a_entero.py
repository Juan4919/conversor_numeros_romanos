from main import romano_a_entero,RomanNumberError
import pytest

def test_romano_a_entero():
    assert romano_a_entero("I") == 1

def test_romano_a_entero_MDCCXIII():
    assert romano_a_entero("MDCCXIII") == 1713

def test_romano_a_entero_IV():
    assert romano_a_entero("IV") == 4    


def test_romano_a_entero_no_repetir_mas_de_tres_01():
    with pytest.raises(RomanNumberError ) as exeptionInfo:
        romano_a_entero("IIII")
    assert str(exeptionInfo.value) == "No se puede repetir el valor mas de tres veces"   


def test_romano_a_entero_no_repetir_mas_de_tres_02():
    with pytest.raises(RomanNumberError ) as exeptionInfo:
        romano_a_entero("XXXX")
    assert str(exeptionInfo.value) == "No se puede repetir el valor mas de tres veces"   

def test_romano_a_entero_no_repetir_mas_de_tres_03():
    with pytest.raises(RomanNumberError ) as exeptionInfo:
        romano_a_entero("CCCC")
    assert str(exeptionInfo.value) == "No se puede repetir el valor mas de tres veces"   

def test_romano_a_entero_no_repetir_mas_de_tres_04():
    with pytest.raises(RomanNumberError ) as exeptionInfo:
        romano_a_entero("MMMM")
    assert str(exeptionInfo.value) == "No se puede repetir el valor mas de tres veces"

def test_romano_a_entero_no_repetir_mas_de_tres_05():
    with pytest.raises(RomanNumberError ) as exeptionInfo:
        romano_a_entero("VV")
    assert str(exeptionInfo.value) == "Los caracteres 'D', 'L' y 'V' no se pueden repetir."

def test_romano_a_entero_no_repetir_mas_de_tres_06():
    with pytest.raises(RomanNumberError ) as exeptionInfo:
        romano_a_entero("LL")
    assert str(exeptionInfo.value) == "Los caracteres 'D', 'L' y 'V' no se pueden repetir." 

def test_romano_a_entero_no_repetir_mas_de_tres_07():
    with pytest.raises(RomanNumberError ) as exeptionInfo:
        romano_a_entero("DD")
    assert str(exeptionInfo.value) == "Los caracteres 'D', 'L' y 'V' no se pueden repetir."

def test_romano_a_entero_restar_solo_de_I_VX():
    with pytest.raises(RomanNumberError ) as exeptionInfo:
        romano_a_entero("IL")
    assert str(exeptionInfo.value) == "I se puede restar de V y X solamente"

def test_romano_a_entero_restar_solo_de_X_LC():
    with pytest.raises(RomanNumberError ) as exeptionInfo:
        romano_a_entero("XM")
    assert str(exeptionInfo.value) == "X se puede restar de L y C solamente"
"""
def test_romano_a_entero_restar_solo_de_C_DM():
    with pytest.raises(RomanNumberError ) as exeptionInfo:
        romano_a_entero("C")
    assert str(exeptionInfo.value) == "'C' se puede restar de 'D' y 'M' solamente"    
"""