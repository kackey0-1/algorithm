
class MyHashSet:
    def __init__(self):
        self.range = 769
        self.hashset = [Bucket() for _ in range(self.range)]

    def _hash(self, value):
        return value % self.range

    def add(self, value):
        index = self._hash(value)
        self.hashset[index].insert(value)

    def remove(self, value):
        index = self._hash(value)
        self.hashset[index].delete(value)

    def contains(self, value):
        index = self._hash(value)
        return self.hashset[index].exists(value)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Bucket:
    def __init__(self):
        self.head = Node(0)

    def insert(self, value):
        if not self.exists(value):
            new_node = Node(value)
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    def delete(self, value):
        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                # remove the current node
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def exists(self, value):
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                return True
            curr = curr.next
        return False


if __name__ == '__main__':
    # Your MyHashSet object will be instantiated and called as such:
    key = 100
    obj = MyHashSet()
    obj.add(key)
    print(obj.contains(key))
    obj.remove(key)
    print(obj.contains(key))
