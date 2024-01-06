from adt import BinaryTreeADT
from node import Node
from queue import Queue


class BinaryTree(BinaryTreeADT):
    def count_node(self, node: Node | None) -> int:
        if node:
            return self.count_node(node.left) + self.count_node(node.right) + 1
        else:
            return 0

    def calc_level(self, node: Node | None) -> int:
        if node:
            left_cnt = self.calc_level(node.left)
            right_cnt = self.calc_level(node.right)
            return max(left_cnt, right_cnt) + 1
        else:
            return 0

    def pre_order(self, node: Node | None):
        if node:
            print(node.data, end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)

    def in_order(self, node: Node | None):
        if node:
            self.in_order(node.left)
            print(node.data, end=" ")
            self.in_order(node.right)

    def post_order(self, node: Node | None):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.data, end=" ")

    def level_order(self, root: Node | None):
        queue = Queue()
        queue.put(root)
        while not queue.empty():
            node = queue.get()
            if node:
                print(node.data, end=" ")
                queue.put(node.left)
                queue.put(node.right)
