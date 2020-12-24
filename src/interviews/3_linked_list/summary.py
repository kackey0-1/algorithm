from __future__ import annotations
from typing import Any


class Node(object):

    def __init__(self, data: Any, next: Node = None, prev: Node = None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList(object):

    def __init__(self, head: Node = None):
        self.head = head

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert(self, data: Any):
        new_node = Node(data)
        current = self.head
        self.head = new_node
        new_node.next = current

    def remove(self, data: Any):
        current = self.head
        if current and current.data == data:
            if current.next is None:
                self.head = None
                current = None
                return
            else:
                self.head = current.next
                current = None
                return

        previous = None
        while current and current.data != data:
            previous = current
            current = current.next

        if current is None:
            return
        if current.next is None:
            previous.next = None
        else:
            previous.next = current.next
        current = None

    def print(self) -> None:
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse_iterative(self) -> None:
        current = self.head
        prev = None
        while current:
            next = current.next

            current.next = prev
            prev = current

            current = next
        self.head = prev

    def reverse_recursive(self):
        def _reverse(current: Node, prev: Node) -> None:
            if current is None:
                self.head = prev
                return
            next = current.next
            current.next = prev
            prev = current
            current = next
            _reverse(current, prev)
        _reverse(self.head, None)


class DoublyLinkedList(object):

    def __init__(self, head: Node = None) -> None:
        self.head = head

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def insert(self, data: Any) -> None:
        new_node = Node(data)
        current = self.head

        self.head = new_node
        new_node.next = current
        if current:
            current.prev = new_node

    def remove(self, data: Any) -> None:
        current = self.head
        if current and current.data == data:
            if current.next is None:
                self.head = None
                return
            else:
                next = current.next
                self.head = next
                next.prev = None
                return

        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current is None:
            return
        if current.next is None:
            prev.next = None
        else:
            next = current.next
            prev.next = next
            next.prev = prev
        current = None

    def print(self) -> None:
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse_iterative(self) -> None:
        current = self.head
        prev = None
        while current:
            prev = current.prev
            current.prev = current.next
            current.next = prev

            current = current.prev
        self.head = prev.prev


if __name__ == '__main__':
    d = DoublyLinkedList()
    d.insert(1)
    d.append(2)
    d.append(3)
    d.insert(0)
    d.remove(0)
    d.remove(2)
    d.remove(3)
    d.append(4)
    d.append(5)
    d.append(6)
    d.print()

    print('#'*100)
    l = LinkedList()
    l.insert(1)
    l.append(2)
    l.append(3)
    l.insert(0)
    l.remove(0)
    l.remove(2)
    l.remove(3)
    l.append(4)
    l.append(5)
    l.append(6)
    l.reverse_iterative()
    l.reverse_recursive()
    l.print()

