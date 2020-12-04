from typing import Any
import hashlib


class HashTable(object):

    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash(self, key) -> int:
        return int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size

    def add(self, key: Any, value: Any) -> None:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                data[1] = value
                break
        else:
            self.table[index].append([key, value])

    def print(self) -> None:
        for index in range(self.size):
            print(index, end=' ')
            for data in self.table[index]:
                print('-->', end=' ')
                print(data, end=' ')

            print()

    def get(self, key) -> Any:
        index = self.hash(key)
        for data in self.table[index]:
            return data[1]

    def __setitem__(self, key, value) -> None:
        self.add(key, value)

    def __getitem__(self, key):
        return self.get(key)


if __name__ == '__main__':
    hash_table = HashTable()
    hash_table['car'] = 'Tesla'
    hash_table['car'] = 'Tesla'
    hash_table['some'] = 'variable'
    hash_table['pc'] = 'Mac'
    hash_table.print()










