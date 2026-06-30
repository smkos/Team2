import pytest

class Calc:
    def getMinus(a: float, b: float):
        return a - b

def test_sample():
    ret = Calc.getMinus(1, 2)
    assert ret == -1