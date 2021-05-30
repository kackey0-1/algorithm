

class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = Node(0)

    def get(self, index: int):
        if self.size < index or index < 0:
            return -1

        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def add_at_index(self, index: int, val):
        if index < 0 or self.size < index:
            return None

        self.size += 1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        new_node = Node(val)
        new_node.prev = curr
        new_node.next = curr.next
        curr.next = new_node

    def add_at_head(self, val):
        self.add_at_index(0, val)

    def add_at_tail(self, val):
        self.add_at_index(self.size, val)


if __name__ == '__main__':

    obj = DoublyLinkedList()
    print('###################')
    print(obj.add_at_head(19))
    print(obj.get(1))
    print('###################')
    print(obj.add_at_tail(9))
    print(obj.get(2))
    print('###################')
    print(obj.add_at_index(0, 2))
    print(obj.get(1))
    print(obj.get(2))
    print(obj.get(3))
    # print(obj.addAtHead(1))
    # print(obj.addAtTail(3))

    # print(obj.get(0))
    # print(obj.deleteAtIndex(1))
    # print(obj.get(1))
    # -------------------------
