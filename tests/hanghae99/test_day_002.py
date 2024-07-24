import pytest


@pytest.mark.parametrize(
    "args",
    [
        (2, 5, [2, 4, 6, 8, 10]),
        (4, 3, [4, 8, 12]),
        (-4, 2, [-4, -8]),
    ],
)
def test_gap_array(args):
    *input, expected = args

    result = solution(*input)

    assert result == expected


def solution(x, n):
    answer = []

    for i in range(1, n + 1):
        answer.append(i * x)

    return answer
