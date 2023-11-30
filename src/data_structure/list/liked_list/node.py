from typing import Self


class Node:
    def __init__(self, item, link: Self | None = None) -> None:
        self.data = item
        self.link = link

    def append(self, node: Self):
        if node is not None:
            node.link = self.link
            self.link = node

    def pop_next(self):
        next = self.link
        if next is not None:
            self.link = next.link

        return next
