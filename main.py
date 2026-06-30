import pytest

class Calc:
    def getZegop(a):
        return a * a


def test_sample():
    zegop_result = Calc().getZegop(3)
    assert zegop_result == 9
    pytest.fail()