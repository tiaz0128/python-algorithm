import pytest
import logging

from src.study.to_be.week_2.solution_1 import solution


@pytest.fixture(
    scope="function", name="nums", params=[[1, 2, 3, 4, 5], [4, 3, 1, 2, 5]]
)
def setup(request):
    return request.param


def test_1(nums):
    # given
    logging.info(nums)

    # when
    result = solution(nums)

    # then
    assert result == [2, 4, 1, 3, 5]
