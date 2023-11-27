def factorial_iter(n):
    if n == 1:
        return 1

    return n * factorial_iter(n - 1)
