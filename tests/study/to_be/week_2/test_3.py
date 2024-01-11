import pytest
import logging

from src.study.to_be.week_2.solution_3 import solution


@pytest.fixture(
    scope="function",
    name="input",
    params=[
        (
            [
                [-1, 0, 0],
                [0, 0, -1],
                [0, -1, 0],
            ],
            [
                [-1, 2, 1],
                [2, 3, -1],
                [1, -1, 2],
            ],
        )
    ],
)
def setup(request):
    return request.param


def test_3(input):
    # given
    grid, expected = input
    logging.info(f"grid={grid}, expected={expected}")

    # when
    result = solution(grid)

    # then
    assert expected == result
