from abc import ABC, abstractmethod


class DequeADT(ABC):
    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def is_full(self) -> bool:
        pass

    @abstractmethod
    def add_front(self, item: any) -> None:
        pass

    @abstractmethod
    def add_rear(self, item: any) -> None:
        pass

    @abstractmethod
    def delete_front(self) -> any:
        pass

    @abstractmethod
    def delete_rear(self) -> any:
        pass

    @abstractmethod
    def get_front(self) -> any:
        pass

    @abstractmethod
    def get_rear(self) -> any:
        pass

    @abstractmethod
    def size(self) -> int:
        pass
