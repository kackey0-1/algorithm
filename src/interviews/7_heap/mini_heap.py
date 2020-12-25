from typing import Optional
import sys


class MiniHeap(object):

    def __init__(self) -> None:
        self.heap = [sys.maxsize * -1]
        self.current_size = 0

    # [-x, 1, 4, 5, 2, 10, 29, 12, 13]
    def parent_index(self, index: int) -> int:
        return index // 2

    def left_child_index(self, index: int) -> int:
        return (index * 2)

    def right_child_index(self, index: int) -> int:
        return (index * 2) + 1


if __name__ == '__main__':
    h = MiniHeap()
    h.heap.append(0)
    h.heap.append(3)
    h.heap.append(5)
    h.heap.append(6)
    h.heap.append(7)

    h.heap.append(8)
    h.heap.append(9)
    print(h.heap)
    print(h.right_child_index(2))
    print(h.heap[h.left_child_index(2)])
    print(h.heap[h.right_child_index(2)])

    print(h.right_child_index(3))
    print(h.heap[h.left_child_index(3)])
    print(h.heap[h.right_child_index(3)])



