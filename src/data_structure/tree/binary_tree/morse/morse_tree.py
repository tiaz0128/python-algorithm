from ..node import Node


class MorseCodeTree:
    def __init__(self, table) -> None:
        self.table = table

        self._make_morse_tree()

    def _make_morse_tree(self) -> None:
        self.root = Node(None, None, None)

        for tp in self.table:
            code = tp[1]
            node = self.root
            for c in code:
                if c == ".":
                    if node.left == None:
                        node.left = Node(None, None, None)
                    node = node.left
                elif c == "-":
                    if node.right == None:
                        node.right = Node(None, None, None)
                    node = node.right
            node.data = tp[0]

    def encode(self, ch):
        idx = ord(ch.upper()) - ord("A")
        return self.table[idx][1]

    def decode(self, code: str):
        node = self.root
        for c in code:
            if c == ".":
                node = node.left
            elif c == "-":
                node = node.right
        return node.data
