from typing import Self


class BTNode:
    def __init__(
        self,
        elem,
        left: Self | None = None,
        right: Self | None = None,
    ) -> None:
        self.data = elem
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None
