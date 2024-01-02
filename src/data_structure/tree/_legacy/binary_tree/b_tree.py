from queue import Queue
from bt_node import BTNode


class BTree:
    def preorder(self, n: BTNode):
        if n is not None:
            print("(", end=" ")
            print(n.data, end=" ")
            self.preorder(n.left)
            self.preorder(n.right)
            print(")", end=" ")

    def inorder(self, n: BTNode):
        if n is not None:
            self.inorder(n.left)
            print(n.data, end=" ")
            self.inorder(n.right)

    def postorder(self, n: BTNode):
        if n is not None:
            self.postorder(n.left)
            self.postorder(n.right)
            print(n.data, end=" ")

    def level_order(self, root: BTNode):
        queue = Queue[BTNode]()
        queue.put(root)
        while not queue.empty():
            n = queue.get()
            if n is not None:
                print(n.data, end=" ")
                queue.put(n.left)
                queue.put(n.right)

    def count_node(self, n: BTNode):
        if n is None:
            return 0

        return self.count_node(n.left) + self.count_node(n.right) + 1

    def calc_height(self, n: BTNode):
        if n is None:
            return 0

        h_left = self.calc_height(n.left)
        h_right = self.calc_height(n.right)

        return max(h_left, h_right) + 1
