from abc import ABC, abstractmethod


class QueueADT(ABC):
    def __init__(self, capacity) -> None:
        self.array = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = 0

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def is_full(self) -> bool:
        pass

    @abstractmethod
    def enqueue(self, item: any) -> None:
        pass

    @abstractmethod
    def dequeue(self) -> any:
        pass

    @abstractmethod
    def peek(self) -> any:
        pass

    @abstractmethod
    def size(self) -> int:
        pass
