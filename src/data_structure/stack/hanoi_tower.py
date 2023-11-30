def hanoi_tower(n, A, B, C):
    if n == 1:
        print(f"원판 1: {A} --> {C}")

    else:
        hanoi_tower(n - 1, A, C, B)
        print(f"원판 {n}: {A} --> {C}")
        hanoi_tower(n - 1, B, A, C)


if __name__ == "__main__":
    hanoi_tower(4, "A", "B", "C")
