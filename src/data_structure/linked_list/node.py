from typing import Self
from adt import NodeADT


class Node(NodeADT):
    def append(self, node: Self) -> None:
        node.link = self.link
        self.link = node

    def pop_next(self) -> Self | None:
        next = self.link
        if next is not None:
            self.link = next.link

        return next
