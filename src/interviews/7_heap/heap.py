import sys
from typing import Optional

class MiniHeap(object):

    def __init__(self):
        self.heap = [-1 * sys.maxsize]
        self.current_size = 0

    def parent_index(self, index: int) -> int:
        return index // 2

    def left_child_index(self, index: int) -> int:
        return 2 * index

    def right_child_index(self, index: int) -> int:
        return (2 * index) + 1

    def swap(self, index: int, index2: int) -> None:
        self.heap[index], self.heap[index2] = self.heap[index2], self.heap[index]

    def heapify_up(self, index: int) -> None:
        while self.parent_index(index) > 0:
            if self.heap[index] < self.heap[self.parent_index(index)]:
                self.swap(index, self.parent_index(index))
            index = self.parent_index(index)

    def push(self, value: int) -> None:
        self.heap.append(value)
        self.current_size += 1
        self.heapify_up(self.current_size)

    def pop(self) -> Optional[int]:
        if len(self.heap) == 1:
            return













if __name__ == '__main__':
    mini_heap = MiniHeap()
    mini_heap.push(5)
    mini_heap.push(6)
    mini_heap.push(2)
    print(mini_heap.heap)







