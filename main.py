import pytest

class Calc:
    def getDivide(self, a, b):
        return a / b

    def getSumSum(self, a, b, c):
        return a + b + c

def test_sample():
    assert 1 == 1
    pytest.fail()