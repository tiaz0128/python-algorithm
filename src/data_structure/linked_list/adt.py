from typing import Self
from abc import ABC, abstractmethod


class NodeADT(ABC):
    def __init__(self, data, link: Self | None = None) -> None:
        self.data = data
        self.link = link

    @abstractmethod
    def append(self, node: Self) -> None:
        pass

    @abstractmethod
    def pop_next(self) -> Self:
        pass


class LinkedListADT(ABC):
    def __init__(self) -> None:
        self.head: NodeADT | None = None

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def is_full(self) -> bool:
        pass

    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def display(self) -> None:
        pass

    @abstractmethod
    def get_node(self, pos: int) -> NodeADT | None:
        pass

    @abstractmethod
    def get_entry(self, pos: int) -> any | None:
        pass

    @abstractmethod
    def insert(self, pos: int, e: any) -> None:
        pass

    @abstractmethod
    def delete(self, pos: int) -> NodeADT | None:
        pass
