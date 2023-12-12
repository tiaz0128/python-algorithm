from binary_tree.bt_node import BTNode

table = [
    ("A", ".-"),
    ("B", "-..."),
    ("C", "-.-."),
    ("D", "-.."),
    ("E", "."),
    ("F", "..-."),
    ("G", "--."),
    ("H", "...."),
    ("I", ".."),
    ("J", ".---"),
    ("K", "-.-"),
    ("L", ".-.."),
    ("M", "--"),
    ("N", "-."),
    ("O", "---"),
    ("P", ".--."),
    ("Q", "--.-"),
    ("R", ".-."),
    ("S", "..."),
    ("T", "-"),
    ("U", "..-"),
    ("V", "...-"),
    ("W", ".--"),
    ("X", "-..-"),
    ("Y", "-.--"),
    ("Z", "--.."),
]


class MorseCodeTree:
    def make_morse_tree(self, table) -> BTNode:
        root = BTNode(None, None, None)
        for tp in table:
            code = tp[1]
            node = root
            for c in code:
                if c == ".":
                    if node.left == None:
                        node.left = BTNode(None, None, None)
                    node = node.left
                elif c == "-":
                    if node.right == None:
                        node.right = BTNode(None, None, None)
                    node = node.right
            node.data = tp[0]
        return root

    def encode(self, ch):
        idx = ord(ch.upper()) - ord("A")
        return table[idx][1]

    def decode(self, root: BTNode, code: str):
        node = root
        for c in code:
            if c == ".":
                node = node.left
            elif c == "-":
                node = node.right
        return node.data


if __name__ == "__main__":
    mc_tree = MorseCodeTree()
    code_tree = mc_tree.make_morse_tree(table)

    str = input("입력 문장 : ")
    mlist = []

    for ch in str:
        code = mc_tree.encode(ch)
        mlist.append(code)

    print("Morse Code: ", mlist)
    print("Decoding  : ", end="")

    for code in mlist:
        ch = mc_tree.decode(code_tree, code)
        print(ch, end="")
    print()
