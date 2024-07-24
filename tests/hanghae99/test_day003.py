import pytest


@pytest.mark.parametrize(
    "args",
    [
        (
            ["sun", "bed", "car"],
            1,
            ["car", "bed", "sun"],
        ),
        (
            ["abce", "abcd", "cdx"],
            2,
            ["abcd", "abce", "cdx"],
        ),
    ],
)
def test_day_003(args):

    *inputs, excepted = args

    result = solution(*inputs)

    assert result == excepted


def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))
