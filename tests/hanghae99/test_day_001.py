import pytest


@pytest.mark.parametrize(
    "n,expected",
    [
        (
            3,
            [
                [1, 2, 3],
                [2, 2, 3],
                [3, 3, 3],
            ],
        ),
        (
            5,
            [
                [1, 2, 3, 4, 5],
                [2, 2, 3, 4, 5],
                [3, 3, 3, 4, 5],
                [4, 4, 4, 4, 5],
                [5, 5, 5, 5, 5],
            ],
        ),
    ],
)
def test_make_n_array(n, expected):
    result = make_n_array(n)

    assert result == expected


def make_n_array(n):
    result = []
    for i in range(n * n):
        div = i // n
        mod = i % n

        if mod == 0:
            result.append([None] * n)

        result[div][mod] = max(div, mod) + 1

    return result


@pytest.mark.parametrize(
    "args",
    [
        (3, 2, 5, [3, 2, 2, 3]),
        (4, 7, 14, [4, 3, 3, 3, 4, 4, 4, 4]),
    ],
)
def test_day_1(args):
    *inputs, expected = args

    answer = solution(*inputs)

    assert expected == answer


def solution(n, left, right):
    answer = []
    for k in range(left, right + 1):
        i = k // n
        j = k % n
        answer.append(max(i, j) + 1)

    return answer
