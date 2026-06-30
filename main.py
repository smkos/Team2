import pytest

class Calc:
    def __init__(self):
        pass
      
    def getDivide(self, a, b):
        return a / b

    def getSumSum(self, a, b, c):
        return a + b + c

    def getSum(self, a, b):
        return a + b

def test_getSum():
    calc = Calc()
    ret = calc.getSum(1, 2)
    assert ret == 3