from __future__ import annotations
from typing import Any


class Node(object):
    def __init__(self, data: Any, prev_node: Node = None, next_node: Node = None) -> None:
        self.data = data
        self.prev = prev_node
        self.next = next_node


class DoublyLinkedList(object):
    def __init__(self, head: Node = None) -> None:
        self.head = head

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def insert(self, data: Any):
        new_node = Node(data)
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next


if __name__ == '__main__':
    l = DoublyLinkedList()
    l.append(1)
    l.append(2)
    l.insert(0)
    l.print()
    print(l.head.data)
    print(l.head.next.data)
    print(l.head.next.prev.data)




















