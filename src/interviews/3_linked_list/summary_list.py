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

    def insert(self, data: Any) -> None:
        new_node = Node(data)
        current = self.head
        self.head = new_node
        new_node.next = current

    def print(self) -> None:
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def remove(self, data: Any) -> None:
        current = self.head
        if current and current.data == data:
            self.head = current.next
            return

        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current is None:
            return
        if current.data == data:
            prev.next = current.next

    def reverse_iterative(self) -> None:
        current = self.head

        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev

    def reverse_recursive(self) -> None:
        def _reverse(current: Node, prev: Node) -> Node:
            if current:
                next = current.next
                current.next = prev
                prev = current
                current = next
                return _reverse(current, prev)
            return prev
        self.head = _reverse(self.head, None)


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
        next = self.head
        self.head = new_node
        new_node.next = next
        if next:
            next.prev = new_node

    def print(self) -> None:
        current = self.head
        while current:
            print(current.data)
            current = current.next

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

    def reverse_iterative(self) -> None:
        current = self.head
        prev = None
        while current:
            current.prev = current.next
            current.next = prev
            prev = current
            current = current.prev
        self.head = prev


if __name__ == '__main__':
    print('#'*100)
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
    d.reverse_iterative()
    d.print()

    print('#'*100)
    print(d.head.data)
    print(d.head.next.data)
    print(d.head.next.next.data)
    print(d.head.next.next.next.data)
    print(d.head.next.next.next.prev.data)
    print(d.head.next.next.next.prev.prev.data)
    print(d.head.next.next.next.prev.prev.prev.data)

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

