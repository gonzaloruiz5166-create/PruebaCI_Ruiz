from funciones import suma, resta

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0

def test_resta():
    assert resta(5, 2) == 3
    assert resta(0, 3) == -3