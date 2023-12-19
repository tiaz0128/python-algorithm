from abc import ABC, abstractmethod


class StackADT(ABC):
    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def is_full(self) -> bool:
        pass

    @abstractmethod
    def push(self, item: any) -> None:
        pass

    @abstractmethod
    def pop(self) -> any:
        pass

    @abstractmethod
    def peek(self) -> any:
        pass

    @abstractmethod
    def size(self) -> int:
        pass
