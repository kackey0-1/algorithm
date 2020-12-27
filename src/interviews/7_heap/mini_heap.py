import sys


class MiniHeap(object):

    def __init__(self) -> None:
        self.heap = [sys.maxsize * -1]
        self.current_size = 0

    def parent_index(self, index: int) -> int:
        return index // 2

    def left_child_index(self, index: int) -> int:
        return index * 2

    def right_chile_index(self, index: int) -> int:
        return (index * 2) + 1

    def push(self, data: int) -> None:
        self.heap.append(data)
        self.current_size += 1
        self.heapify_up(self.current_size)

    def heapify_up(self, index: int) -> None:
        parent_index = self.parent_index(index)
        while self.heap[index] < self.heap[parent_index]:
            print(self.heap[index], self.heap[parent_index])
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = self.parent_index(parent_index)


if __name__ == '__main__':
    h = MiniHeap()
    h.push(9)
    h.push(1)
    h.push(4)
    print(h.parent_index(3))
    print(h.heap)




