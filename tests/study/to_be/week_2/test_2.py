import pytest
import logging

from src.study.to_be.week_2.solution_2 import solution_2


@pytest.fixture(
    scope="function", name="input", params=[([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3])]
)
def setup(request):
    return request.param


def test_2(input):
    # given
    nums, k, answer = input
    logging.info(f"nums={nums}, k={k}, answer={answer}")

    # when
    result = solution_2(nums, k)

    # then
    assert answer == result
