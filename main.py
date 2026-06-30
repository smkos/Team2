import pytest

class Calc:
    def getGop(self, a: float, b: float) -> float:
        return a * b

@pytest.mark.parametrize('a,b,expected', [(1,2,2), (2,3,6)])
def test_getGop(a, b, expected):
    cal = Calc()
    assert cal.getGop(a, b) == expected
