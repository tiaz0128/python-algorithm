from collections import deque


def solution_1(nums: list[int], k: int) -> list[int]:
    length = len(nums)
    return [nums[(length - k + i) % length] for i in range(length)]


def solution_2(nums: list[int], k: int) -> list[int]:
    answer = deque(nums)

    for _ in range(k):
        last_num = answer.pop()
        answer.insert(0, last_num)

    return list(answer)
