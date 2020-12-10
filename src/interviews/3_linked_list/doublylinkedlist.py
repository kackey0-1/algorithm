from typing import Any


class Node(object):

    def __init__(self, value: Any):
        self.data = value
        self.next = None
        self.prev = None


class DoublyLinkedList(object):

    def __init__(self):
        self.head = None

    def append(self, value: Any) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current

    def print(self) -> None:
        if self.head is None:
            return

        current = self.head
        while current:
            print(current.data)
            current = current.next

    def remove(self, value: Any) -> Node:
        current = self.head
        next = None
        prev = None
        while current.next:
            pass


if __name__ == '__main__':
    d = DoublyLinkedList()
    d.add(10)
    d.add(8)
    d.add(4)
    d.add(12)
    d.add(93)
    d.print()




