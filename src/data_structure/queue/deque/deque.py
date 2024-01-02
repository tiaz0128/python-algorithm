from adt import DequeADT


class Deque(DequeADT):
    def is_empty(self) -> bool:
        return self.front == self.rear

    def is_full(self) -> bool:
        return self.front == (self.rear + 1) % self.capacity

    def size(self) -> int:
        return (self.front - self.rear + self.capacity) % self.capacity

    def add_rear(self, item: any) -> None:
        self.rear = (self.rear + 1) % self.capacity
        self.array[self.rea] = item

        if self.is_empty():
            self.front = (self.front + 1) % self.capacity

    def add_front(self, item: any) -> None:
        if not self.is_full():
            self.array[self.front] = item
            self.front = (self.front - 1 + self.capacity) % self.capacity

    def delete_front(self) -> any:
        if not self.is_empty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]

    def delete_rear(self) -> any:
        if not self.is_empty():
            item = self.array[self.rear]
            self.rear = (self.rear - 1 + self.capacity) % self.capacity

            return item

    def get_front(self) -> any:
        return self.array[(self.rear + 1) % self.capacity]

    def get_rear(self) -> any:
        if not self.is_empty():
            return self.array[self.rear]

    def display(self):
        for i in range(self.front + 1, self.front + 1 + self.capacity):
            print(self.array[i % self.capacity])
