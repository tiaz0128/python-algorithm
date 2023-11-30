from queue import Queue


def fibonacci(n):
    # 큐 초기화
    q = Queue()
    q.put(0)
    q.put(1)

    for _ in range(n):
        # 첫 번째 수를 꺼내고
        first = q.get()
        # 두 번째 수를 확인
        second = q.queue[0]
        # 두 수의 합을 계산
        next_fib = first + second
        # 다음 피보나치 수를 큐에 추가
        q.put(next_fib)

    # n번째 피보나치 수 반환
    return q.get()


# 예시: 10번째 피보나치 수 계산
print(fibonacci(3))
