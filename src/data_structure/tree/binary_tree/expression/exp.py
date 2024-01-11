from ..node import Node


class _TREE:
    def evaluate(self, node: Node):
        if node is None:
            return 0
        elif node.is_leaf():
            return node.data
        else:
            op1 = self.evaluate(node.left)
            op2 = self.evaluate(node.right)
            if node.data == "+":
                return op1 + op2
            if node.data == "-":
                return op1 - op2
            if node.data == "*":
                return op1 * op2
            if node.data == "/":
                return op1 / op2

    def build_tree(self, expr: list):
        if len(expr) == 0:
            return None

        token = expr.pop()

        if token in ("+", "-", "*", "/"):
            node = Node(token)
            node.right = self.build_tree(expr)
            node.left = self.build_tree(expr)
        else:
            return Node(float(token))
