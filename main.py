import pytest

class Calc:
    def getZegop(a):
        return a * a


def test_zegop():
    calc = Calc()
    ret = calc.getZegop(3)
    assert ret == 9