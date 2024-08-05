import pytest

@pytest.mark.parametrize(
    "n,expected",
    [
        (["muzi", "ryan", "frodo", "neo"]	["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]	,2),
        (["joy", "brad", "alessandro", "conan", "david"]	["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]	,4),
        (["a", "b", "c"]	["a b", "b a", "c a", "a c", "a c", "c a"]	,0),
)
def test_most_presented_gift():
    pass