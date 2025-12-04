from collections import deque


def is_mango_seller(name):
    return name.startswith("X")


def find_nearest_seller(graph, start_node):
    search_queue = deque([start_node])
    checked = {start_node}

    while search_queue:
        person = search_queue.popleft()

        if is_mango_seller(person):
            return person

        if person in graph:
            for neighbor in graph[person]:
                if neighbor not in checked:
                    search_queue.append(neighbor)
                    checked.add(neighbor)

    return None


# 그래프 정의
network = {
    "나": ["영희", "철수", "민수"],
    "영희": ["재민"],
    "철수": ["토마스", "아름"],  # 아름: 판매자
    "민수": ["지호"],
    "재민": ["하람"],  # 하람: 판매자
    "토마스": [],
    "아름": [],
    "지호": [],
    "하람": [],
}

# 탐색 시작!
result = find_nearest_seller(network, "나")

print(f"가장 가까운 망고 상인: {result}")
