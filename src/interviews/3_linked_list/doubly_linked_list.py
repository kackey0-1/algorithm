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
        if self.head is None:
            self.head = new_node
            return

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def print(self):
        print('#' * 50)
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove(self, value: Any) -> None:
        current_node = self.head
        if current_node is None:
            if current_node.data == value:
                current_node = None
                self.head = current_node
                return
        else:
            if current_node.data == value:
                self.head = current_node.next
                current_node = None
                return

        while current_node.next:
            if current_node.data == value:
                prev_node = current_node.prev
                next_node = current_node.next
                prev_node.next = next_node
                next_node.prev = prev_node
                current_node = None
                return
            current_node = current_node.next

        if current_node and current_node.data == value:
            prev_node = current_node.prev
            prev_node.next = current_node.next
            current_node = None
            return







if __name__ == '__main__':
    d = DoublyLinkedList()
    d.append(0)
    d.append(1)
    d.append(2)
    d.append(3)
    d.print()
    d.remove(4)
    d.print()




















