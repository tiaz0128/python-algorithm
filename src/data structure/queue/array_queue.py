class ArrayQueue:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return self.front == (self.rear + 1) % self.capacity

    def enqueue(self, item):
        if not self.is_full():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item

    # ring buffer
    def enqueue2(self, item):
        self.rear = (self.rear + 1) % self.capacity
        self.array[self.rear] = item

        if self.front == self.rear:
            self.front = (self.front + 1) % self.capacity

    def dequeue(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]

    def peek(self):
        if not self.is_empty():
            return self.array[(self.front + 1) % self.capacity]

    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity

    def display(self):
        print()
        for i in range(self.front + 1, self.front + 1 + self.capacity):
            print(i % self.capacity, self.array[i % self.capacity])
