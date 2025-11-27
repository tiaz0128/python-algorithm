def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# 테스트
data = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(selection_sort(data))
# 출력: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
