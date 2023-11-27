class ArrayStack:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, item):
        if not self.is_full():
            self.array[self.top] = item
            self.top = self.top + 1

    def pop(self):
        if not self.is_empty():
            ret = self.array[self.top]
            self.top = self.top - 1
            return ret

    def peek(self):
        if not self.is_empty():
            return self.array[self.top]
