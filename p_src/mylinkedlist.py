
class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode


class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.head = Node(0)

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list.
        If the index is invalid, return -1.
        """
        if index < 0 or self.size <= index:
            return -1
        curr = self.head
        for _ in range(index + 1):
            curr = curr.next
        return curr.value

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """
        if self.size < index:
            return
        if index < 0:
            return

        new_node = Node(val)
        curr = self.head
        for _ in range(index):
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return

        curr = self.head
        for _ in range(index):
            curr = curr.next
        curr.next = curr.next.next
        self.size -= 1


if __name__ == '__main__':
    # Your MyLinkedList object will be instantiated and called as such:
    # ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
    # [[],[1],[3],[1,2],[1],[1],[1]]
    # -------------------------------------------------------
    # ["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
    # [[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]
    # -------------------------------------------------------
    # ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
    # [[],[1],[3],[1,2],[1],[1],[1]]

    obj = MyLinkedList()
    # print(obj.addAtHead(1))
    # print(obj.addAtTail(3))
    # print(obj.addAtIndex(1, 2))
    # print(obj.get(1))
    # print(obj.deleteAtIndex(1))
    # print(obj.get(1))
    # -------------------------------------------------------
    print(obj.addAtHead(7))
    print(obj.addAtHead(2))
    print(obj.addAtHead(1))
    print(obj.addAtIndex(3, 0))
    print(obj.deleteAtIndex(2))
    print(obj.addAtHead(6))
    print(obj.addAtTail(4))
    print(obj.get(4))
    print(obj.addAtHead(4))
    print(obj.addAtIndex(5, 0))
    print(obj.addAtHead(6))
