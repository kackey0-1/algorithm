import hashlib


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = self.hash(key)
        for t in self.table[index]:
            if t[0] == key:
                t[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = self.hash(key)
        for t in self.table[index]:
            if t[0] == key:
                return t[1]
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = self.hash(key)
        for i, t in enumerate(self.table[index]):
            if t[0] == key:
                self.table[index].pop(i)

    def hash(self, key) -> int:
        return int(hashlib.sha256(str(key).encode()).hexdigest(), base=16) % 10