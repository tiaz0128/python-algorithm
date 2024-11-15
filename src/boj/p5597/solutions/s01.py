def solution():
    a = set(range(1, 31))
    b = {int(input()) for _ in range(28)}

    print(*sorted(a - b), sep="\n")
