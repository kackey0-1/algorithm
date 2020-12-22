from typing import Any
import hashlib


class HashTable(object):

    def __init__(self, size: int = 10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key: str) -> int:
        return int(hashlib.md5(key.encode()).hexdigest(), base=16) % 10

    def add(self, key: Any, value: Any) -> None:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                data[1] = value
                return
        else:
            self.table[index].append([key, value])

    def get(self, key: str) -> Any:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                return data[1]

    def __getitem__(self, key: Any) -> Any:
        return self.get(key)

    def __setitem__(self, key: Any, value: Any) -> None:
        self.add(key, value)

    def print(self) -> None:
        for i in range(len(self.table)):
            print(i, end=' ')
            for data in self.table[i]:
                print('-->', end=' ')
                print(data, end=' ')
            print()


if __name__ == '__main__':
    h = HashTable()
    h['car'] = 'Tesla'
    h['car'] = 'Toyota'
    h['language'] = 'Python'
    h['pc'] = 'Mac'
    h['sns'] = 'Facebook'
    print(h['pc'])
    h.print()






