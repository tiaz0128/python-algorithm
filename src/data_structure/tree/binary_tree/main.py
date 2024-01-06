from tree import BinaryTree
from node import Node

if __name__ == "__main__":
    d = Node("D")
    e = Node("E")
    b = Node("B", d, e)
    f = Node("F")
    c = Node("C", f)
    root = Node("A", b, c)

    tree = BinaryTree()

    print("==pre_order==")
    tree.pre_order(root)

    print("\n==in_order==")
    tree.in_order(root)

    print("\n==post_order==")
    tree.post_order(root)

    print("\n==pre_order==")
    tree.level_order(root)

    print("\n==count node==")
    print(tree.count_node(root))

    print("==calc level==")
    print(tree.calc_level(root))
