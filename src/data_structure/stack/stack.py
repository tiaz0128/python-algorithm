from adt import StackADT


class Stack(StackADT):
    def __init__(self, capacity) -> None:
        super().__init__()

        self.array = [None] * capacity
        self.capacity = capacity
        self.top = -1

    def is_empty(self) -> bool:
        return self.top == -1

    def is_full(self) -> bool:
        return self.top == self.capacity

    def push(self, item: any) -> None:
        if not self.is_full():
            self.top += 1
            self.array[self.top] = item

    def pop(self) -> any:
        if not self.is_empty():
            item = self.array[self.top]
            self.top -= 1
            return item

    def peek(self):
        return self.array[self.top]

    def size(self):
        return self.top + 1
