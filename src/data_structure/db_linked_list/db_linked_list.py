from adt import LinkedListADT, NodeADT
from db_node import DoubleNode


class DoubleLinkedList(LinkedListADT):
    def is_empty(self) -> bool:
        return self.head is None

    def is_full(self) -> bool:
        return False

    def size(self) -> int:
        ptr = self.head
        cnt = 0
        while ptr is not None:
            cnt += 1
            ptr = ptr.next

        return cnt

    def display(self) -> None:
        ptr = self.head

        while ptr is not None:
            print(ptr.data)
            ptr = ptr.link
        print("None")

    def get_node(self, pos: int) -> NodeADT | None:
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
        node = DoubleNode(e)
        before = self.get_node(pos - 1)

        if before is None:
            node.next = self.head
            if node.next is not None:
                node.next.prev = node
        else:
            before.append(node)

    def delete(self, pos: int) -> NodeADT | None:
        before = self.get_node(pos - 1)

        if before is None:
            before = self.head
            if self.head is not None:
                self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return before
        else:
            before.pop_next()
