from typing import Any


class Node(object):

    def __init__(self, data: Any):
        self.data = data
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.head = None

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def print(self) -> None:
        if self.head is None:
            return
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove(self, data: Any) -> Any:
        if self.head.next is None and self.head.data == data:
            self.head = None
            return

        current_node = self.head
        previous_node = None
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        previous_node.next = current_node.next
        current_node = None

    def reverse_iterative(self) -> None:
        previous_node = None
        current_node = self.head

        while current_node:
            next_node = current_node.next
            current_node.next = previous_node

            previous_node = current_node
            current_node = next_node

        self.head = previous_node


if __name__ == '__main__':
    l = LinkedList()
    l.add(6)
    l.add(19)
    l.add(20)
    l.add(1)
    # print(l.head.data)
    # print(l.head.next.data)
    # print(l.head.next.next.data)
    # l.remove(19)
    l.reverse_iterative()
    l.print()

