from bt_node import BTNode
from b_tree import BTree


if __name__ == "__main__":
    d = BTNode("D", None, None)
    e = BTNode("E", None, None)
    b = BTNode("B", d, e)
    f = BTNode("F", None, None)
    c = BTNode("C", f, None)
    root = BTNode("A", b, c)

    b_tree = BTree()

    print("\n   In-Order : ", end="")
    b_tree.inorder(root)

    print("\n  Pre-Order : ", end="")
    b_tree.preorder(root)

    print("\n Post-Order : ", end="")
    b_tree.postorder(root)

    print("\nLevel-Order : ", end="")
    b_tree.level_order(root)
    print("\n")

    print(f"노드의 개수 = {b_tree.count_node(root)}개")
    print(f"트리의 높이 = {b_tree.calc_height(root)}")
