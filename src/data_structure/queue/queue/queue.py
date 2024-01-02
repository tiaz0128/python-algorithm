from adt import QueueADT


class Queue(QueueADT):
    def is_empty(self) -> bool:
        return self.front == self.rear

    def is_full(self) -> bool:
        return self.front == (self.rear + 1) % self.capacity

    def enqueue(self, item: any) -> None:
        self.rear = (self.rear + 1) % self.capacity
        self.array[self.rear] = item
        if not self.is_empty():
            self.front = (self.front + 1) % self.capacity

    def dequeue(self) -> any:
        if not self.is_empty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]

    def peek(self) -> any:
        if not self.is_empty():
            return self.array[(self.front + 1) % self.capacity]

    def size(self) -> int:
        return (self.front - self.rear + self.capacity) % self.capacity

    def display(self) -> None:
        for i in range(self.front + 1, self.front + 1 + self.size()):
            print(self.array[i % self.capacity])
