from typing import Self
from adt import NodeADT


class DoubleNode(NodeADT):
    def append(self, node: Self) -> None:
        if node is not None:
            node.next = self.next
            node.prev = self
            if node.next is not None:
                node.next.prev = node
            self.next = node

    def pop_next(self) -> Self | None:
        node = self.next
        if node is not None:
            self.next = node.next
            if node.next is not None:
                self.next.prev = self
        return node
