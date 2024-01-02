import sys
from pathlib import Path


path = str(Path(__file__).parent.parent / "binary_tree")
sys.path.append(path)


from bt_node import BTNode


def evaluate(node: BTNode):
    if node is None:
        return 0
    elif node.is_leaf():
        return node.data
    else:
        op1 = evaluate(node.left)
        op2 = evaluate(node.right)
        if node.data == "+":
            return op1 + op2
        if node.data == "-":
            return op1 - op2
        if node.data == "*":
            return op1 * op2
        if node.data == "/":
            return op1 / op2


def build_tree(expr: list):
    if len(expr) == 0:
        return None

    token = expr.pop()

    if token in ("+", "-", "*", "/"):
        node = BTNode(token)
        node.right = build_tree(expr)
        node.left = build_tree(expr)
    else:
        return BTNode(float(token))
