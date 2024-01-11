import pytest
import logging

from src.study.to_be.week_2.solution_1 import solution


@pytest.fixture(
    scope="function",
    name="test_input",
    params=[
        ([1, 2, 3, 4, 5], [2, 4, 1, 3, 5]),
        ([4, 3, 1, 2, 5], [2, 4, 1, 3, 5]),
    ],
)
def setup(request):
    return request.param


def test_1(test_input):
    # given
    nums, expected = test_input

    # when
    result = solution(nums)

    # then
    assert result == expected
