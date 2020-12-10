from typing import Any
import hashlib


class HashTable(object):

    def __init__(self):
        self.size = 10
        self.table = [[] for i in range(self.size)]

    def hash(self, key) -> int:
        return int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size

    def add(self, key, value) -> None:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                data[1] = value
                break
        else:
            self.table[index].append([key, value])

    def get(self, key) -> Any:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                return data[1]
        return None

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key) -> Any:
        return self.get(key)


if __name__ == '__main__':
    h = HashTable()
    # print(h.table)
    # print(h.hash('car'))
    # print(h.hash('pc'))
    # print(h.hash('language'))
    # print(h.hash('sns'))
    # h.add('pc', 'Mac')
    # h.add('car', 'Tesla')
    # h.add('language', 'Python')
    # h.add('sns', 'Twitter')
    h['car'] = 'Tesla'
    h['language'] = 'Python'
    h['sns'] = 'Facebook'
    h['pc'] = 'Mac'
    print(h.table)
    print(h['pc'])
    print(h['sns'])
    print(h['hoge'])





