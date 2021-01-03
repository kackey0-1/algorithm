from typing import Optional
import sys


class MiniHeap(object):

    def __init__(self) -> None:
        self.heap = [sys.maxsize * -1]
        self.current_size = 0

    def parent_index(self, index: int) -> int:
        return index // 2

    def left_child_index(self, index: int) -> int:
        return (index * 2)

    def right_child_index(self, index: int) -> int:
        return (index * 2) + 1

    def swap(self, index1: int, index2: int) -> None:
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def heapify_up(self, index: int) -> None:
        parent_index = self.parent_index(index)
        while self.heap[index] < self.heap[parent_index]:
            self.swap(index, parent_index)
            index = parent_index
            parent_index = self.parent_index(parent_index)

    def push(self, value: int) -> None:
        self.heap.append(value)
        self.current_size += 1
        self.heapify_up(self.current_size)

    def min_child_index(self, index: int):
        if self.right_child_index(index) > self.current_size:
            return self.left_child_index(index)
        else:
            if self.heap[self.left_child_index(index)] < self.heap[self.right_child_index(index)]:
                return self.left_child_index(index)
            else:
                return self.right_child_index(index)

    def heapify_down(self, index: int) -> None:
        while self.left_child_index(index) <= self.current_size:
            min_child_index = self.min_child_index(index)
            if self.heap[index] > self.heap[min_child_index]:
                self.swap(index, min_child_index)
            index = min_child_index

    def pop(self) -> Optional[int]:
        if len(self.heap) == 1:
            return

        root = self.heap[1]
        data = self.heap.pop()
        self.current_size -= 1
        if len(self.heap) == 1:
            return root

        self.heap[1] = data
        self.heapify_down(1)
        return root


if __name__ == '__main__':
    h = MiniHeap()
    h.push(8)
    h.push(9)
    h.push(0)
    h.push(1)
    h.push(4)
    print(h.heap)
    h.push(2)

    print(h.heap)
    print(h.pop())
    print(h.heap)
    print(h.pop())
    print(h.heap)




