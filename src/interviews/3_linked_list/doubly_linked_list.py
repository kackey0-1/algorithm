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

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node

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
        if current_node and current_node.data == value:
            if current_node.next is None:
                current_node = None
                self.head = None
                return
            else:
                self.head = current_node.next
                current_node = None
                return

        while current_node and current_node.data != value:
            current_node = current_node.next

        if current_node is None:
            return

        if current_node.next is None:
            prev = current_node.prev
            prev.next = None
            current_node = None
        else:
            prev_node = current_node.prev
            next_node = current_node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            current_node = None
            return

        """
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
        """
    def reverse_iterative(self) -> None:
        # TODO need to re-try
        previous_node = None
        current_node = self.head
        while current_node:
            previous_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = previous_node

            current_node = current_node.prev

        if previous_node:
            self.head = previous_node.prev

    def reverse_recursive(self) -> None:
        # TODO need to re-try
        def _reverse(current_node: Node, previous_node: Node):
            if current_node is None:
                if previous_node:
                    self.head = previous_node.prev
                return
            previous_node = current_node.prev
            current_node.prev = current_node.next
            current_node.next = previous_node

            current_node = current_node.prev
            return _reverse(current_node, previous_node)

        previous_node = None
        current_node = self.head
        _reverse(current_node, previous_node)

    def sort(self) -> None:
        if self.head is None:
            return

        current_node = self.head
        while current_node.next:
            next_node = current_node.next
            while next_node:
                if current_node.data > next_node.data:
                    next_node.data, current_node.data = current_node.data, next_node.data
                next_node = next_node.next
            current_node = current_node.next


if __name__ == '__main__':
    d = DoublyLinkedList()
    d.append(3)
    d.append(13)
    d.append(1)
    d.append(6)
    d.append(8)
    # d.reverse_iterative()
    # d.print()
    # d.reverse_recursive()
    d.print()
    d.sort()
    d.print()




















