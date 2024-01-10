def solution(nums: list[int]) -> list[int]:
    sorted_nums = sorted(nums)

    even_nums = [num for num in sorted_nums if num % 2 == 0]
    odd_nums = [num for num in sorted_nums if num % 2 == 1]

    return even_nums + odd_nums
