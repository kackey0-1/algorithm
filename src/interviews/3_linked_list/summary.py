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

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node
        new_node.prev = current_node


if __name__ == '__main__':

    # l = LinkedList()
    # l.insert(0)
    # l.append(2)
    # l.append(4)
    # l.insert(19)
    # l.append(1)
    # l.append(2)
    # l.append(3)
    # l.append(4)
    # l.reverse_recursive()
    # l.print()

    d = DoublyLinkedList()
    d.append(0)
    d.append(1)
    d.append(2)
    print(d.head.data)
    print(d.head.next.data)
    print(d.head.next.next.data)
    print(d.head.next.next.prev.data)
    print(d.head.next.next.prev.prev.data)









