from typing import Any


class Node(object):

    def __init__(self, data: Any, next=None, prev=None):
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
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        return

    def insert(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        self.head = new_node
        new_node.next = current_node
        return

    def remove(self, data: Any):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            current = None
            return

        previous = None
        while current and current.data != data:
            previous = current
            current = current.next

        if current is None:
            return

        if current.data == data:
            previous.next = current.next
            current = None

    def print(self) -> None:
        if self.head is None:
            return
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def reverse_iterative(self) -> None:
        current_node = self.head
        previous_node = None
        while current_node:
            next_node = current_node.next

            current_node.next = previous_node
            previous_node = current_node

            current_node = next_node
        self.head = previous_node

    def reverse_recursive(self) -> None:
        def _reverse(current_node, previous_node) -> None:
            if current_node is None:
                self.head = previous_node
                return
            next_node = current_node.next

            current_node.next = previous_node
            previous_node = current_node

            current_node = next_node
            _reverse(current_node, previous_node)

        _reverse(self.head, None)


class DoublyLinkedList(object):

    def __init__(self, head=None):
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
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        self.head = new_node
        new_node.next = current
        current.prev = new_node

    def print(self) -> None:
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def remove(self, data: Any) -> None:
        current = self.head
        if current and current.data == data:
            if current.next is None:
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

        if current.data == data:
            next_node = current.next
            previous.next = next_node
            next_node.prev = previous
            current = None

    def reverse_iterative(self) -> None:
        current = self.head
        prev_node = None

        while current:
            prev_node = current.prev
            current.prev = current.next
            current.next = prev_node

            current = current.prev
        if prev_node:
            self.head = prev_node.prev


if __name__ == '__main__':
    l = LinkedList()
    l.insert(0)
    l.append(2)
    l.append(3)
    l.insert(19)
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(8)
    l.remove(1)
    l.reverse_recursive()
    l.remove(8)
    l.print()
    print('#'*100)

    d = DoublyLinkedList()
    d.insert(0)
    d.append(1)
    d.append(2)
    d.insert(4)
    # d.remove(0)
    d.reverse_iterative()
    d.print()







