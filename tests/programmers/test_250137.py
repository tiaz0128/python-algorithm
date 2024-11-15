import pytest

from programmers.p250137.solutions.s01 import solution


@pytest.mark.parametrize(
    "args",
    [
        ([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]], 5),
        ([3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]], -1),
        ([4, 2, 7], 20, [[1, 15], [5, 16], [8, 6]], -1),
        ([1, 1, 1], 5, [[1, 2], [3, 2]], 3),
    ],
)
def test_battle_simulation(args):
    *inputs, expected = args

    result = solution(*inputs)

    assert expected == result
