from typing import Any, Optional
import hashlib


class HashTable(object):

    def __init__(self, size: int = 10) -> None:
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, value: Any) -> int:
        return int(hashlib.md5(value.encode()).hexdigest(), base=16) % 10

    def add(self, key: Any, value: Any) -> None:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                data[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key: Any) -> Optional[Any]:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                return data[1]

    def print(self) -> None:
        for i in range(len(self.table)):
            print(i, end=' ')
            for data in self.table[i]:
                print('-->', end=' ')
                print(data, end=' ')
            print()


    def __setitem__(self, key, value) -> None:
        self.add(key, value)

    def __getitem__(self, key) -> Optional[Any]:
        return self.get(key)


if __name__ == '__main__':
    h = HashTable()
    # h.add('car', 'Tesla')
    h['car'] = 'Tesla'
    # h.add('car', 'Toyota')
    h['car'] = 'Toyota'
    # h.add('language', 'Python')
    h['language'] = 'Python'
    # h.add('pc', 'Mac')
    h['pc'] = 'Mac'
    # h.add('sns', 'Facebook')
    h['sns'] = 'Facebook'
    print(h['car'])
    print(h['get'])
    print(h.table)
    h.print()






