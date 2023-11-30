from array_queue import ArrayQueue


class CircularDeque(ArrayQueue):
    def __init__(self, capacity) -> None:
        super().__init__(capacity)

    def add_rear(self, item):
        self.enqueue(item)

    def add_rear2(self, item):
        self.enqueue2(item)

    def delete_front(self):
        return self.dequeue()

    def get_front(self):
        return self.peek()

    def add_front(self, item):
        if not self.is_full():
            self.array[self.front] = item
            self.front = (self.front - 1 + self.capacity) % self.capacity

    def add_front2(self, item):
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.array[self.front] = item

        if self.front == self.rear:
            self.rear = (self.rear - 1 + self.capacity) % self.capacity

    def delete_rear(self):
        if not self.is_empty():
            item = self.array[self.rear]
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
            return item

    def get_rear(self):
        if not self.is_empty():
            return self.array[self.rear]


deque = CircularDeque(5)

deque.add_front2(1)
deque.add_front2(2)
deque.add_front2(3)
deque.add_front2(4)
deque.add_front2(5)
# deque.add_front2(6)

deque.display()
