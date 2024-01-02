from adt import LinkedListADT
from linked_list.adt import NodeADT
from node import Node


class LinkedList(LinkedListADT):
    def is_empty(self) -> bool:
        return self.head is None

    def is_full(self) -> bool:
        return False

    def size(self) -> int:
        ptr = self.head
        cnt = 0
        while ptr is not None:
            cnt += 1
            ptr = ptr.link

        return cnt

    def display(self) -> None:
        ptr = self.head

        while ptr is not None:
            print(ptr.data)
            ptr = ptr.link
        print("None")

    def get_node(self, pos: int) -> Node | None:
        if pos < 0:
            return None
        ptr = self.head

        for _ in range(pos):
            if ptr is None:
                return None

            ptr = ptr.link
        return ptr

    def get_entry(self, pos: int) -> any | None:
        node = self.get_node(pos)

        return None if node is None else node.data

    def insert(self, pos: int, e: any) -> None:
        node = Node(e, None)
        before = self.get_node(pos - 1)

        if before is None:
            node.link = self.head
            self.head = node
        else:
            before.append(node)

    def delete(self, pos: int) -> NodeADT | None:
        before = self.get_node(pos - 1)

        if before is None:
            before = self.head
            if before is not None:
                self.head = before.link
            return before
        else:
            return before.pop_next()
