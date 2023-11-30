from node import Node


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None

    def is_empty(self):
        return self.head is None

    def is_full(self):
        return False

    def clear(self):
        self.head = None

    def find(self, val):
        node = self.head
        while node is not None:
            if node.data == val:
                return node
            node = node.link
        return node

    def get_node(self, pos) -> Node | None:
        if pos < 0:
            return None

        ptr = self.head

        for _ in range(pos):
            if ptr is None:
                return None
            ptr = ptr.link

        return ptr

    def get_entry(self, pos):
        node = self.get_node(pos)

        if node is None:
            return None

        return node.data

    def insert(self, pos, item) -> None:
        before = self.get_node(pos - 1)
        insert_node = Node(item, None)

        if before is None:
            insert_node.link = self.head
            self.head = insert_node
        else:
            before.append(insert_node)

    def delete(self, pos):
        before = self.get_node(pos - 1)

        if before is None:
            head = self.head
            if not self.is_empty():
                self.head = self.head.link
            return head
        else:
            return before.pop_next()

    def size(self):
        ptr = self.head
        cnt = 0

        while ptr is not None:
            ptr = ptr.link
            cnt = cnt + 1

        return cnt

    def replace(self, pos, elem):
        node = self.get_node(pos)
        if node != None:
            node.data = elem

    def display(self, msg="LinkedList:"):
        print(msg, end="")
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end="->")
            ptr = ptr.link
        print("None")
