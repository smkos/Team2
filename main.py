import pytest

class Calc:
    def __init__(self):
        pass
    
    def getMinus(self, a: float, b: float):
        return a - b
      
    def getDivide(self, a, b):
        return a / b

    def getSumSum(self, a, b, c):
        return a + b + c

    def getSum(self, a, b):
        return a + b
      
    def getGop(self, a: float, b: float) -> float:
        return a * b
      
def test_getSum():
    calc = Calc()
    ret = calc.getSum(1, 2)
    assert ret == 3
    
def test_minus():
    calc = Calc()
    ret = calc.getMinus(1, 2)
    assert ret == -1

    
@pytest.mark.parametrize('a,b,expected', [(1,2,2), (2,3,6)])
def test_getGop(a, b, expected):
    cal = Calc()
    assert cal.getGop(a, b) == expected
