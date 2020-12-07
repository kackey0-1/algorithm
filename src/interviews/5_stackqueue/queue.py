from collections import deque
from typing import Any


class Queue(object):
    # class collections.deque
    def __init__(self):
        self.queue = []

    def enqueue(self, data: Any) -> None:
        self.queue.append(data)

    def dequeue(self) -> Any:
        if self.queue:
            return self.queue.pop(0)


def reverse(queue: deque) -> deque:
    new_queue = deque()
    while queue:
        new_queue.append(queue.pop())
    [queue.append(d) for d in new_queue]
    # return new_queue


if __name__ == '__main__':
    # queue = Queue()
    # queue.enqueue(1)
    # print(queue.queue)
    # queue.enqueue(2)
    # queue.enqueue(3)
    # queue.enqueue(4)
    # print(queue.queue)
    # queue.dequeue()
    # print(queue.queue)
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)
    print(q)
    reverse(q)
    print(q)
    # print(q.popleft())
    # print(q)
