from node import Node
from abc import ABC, abstractmethod


class BinaryTreeADT(ABC):
    @abstractmethod
    def count_node(self, node: Node | None) -> int:
        pass

    @abstractmethod
    def calc_level(self, node: Node | None) -> int:
        pass

    @abstractmethod
    def pre_order(self, node: Node | None):
        pass

    @abstractmethod
    def in_order(self, node: Node | None):
        pass

    @abstractmethod
    def post_order(self, node: Node | None):
        pass

    @abstractmethod
    def level_order(self, root: Node | None):
        pass
