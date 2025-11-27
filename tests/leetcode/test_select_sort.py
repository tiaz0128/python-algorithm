import pytest


@pytest.mark.parametrize(
    "args",
    [
        ([5, 3, 6, 2, 10], [2, 3, 5, 6, 10]),
    ],
)
def test_select_sort(args):
    *inputs, expected = args

    result = solutions(*inputs)

    assert expected == result


def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index


def solutions(arr):
    new_arr = []
    copied_arr = list(arr)

    for i in range(len(copied_arr)):
        smallest = find_smallest(copied_arr)
        new_arr.append(copied_arr.pop(smallest))

    return new_arr
