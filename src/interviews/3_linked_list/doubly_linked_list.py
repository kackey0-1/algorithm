from __future__ import annotations
from typing import Any


class Node(object):
    def __init__(self, data: Any, previous_node: Node = None, next_node: Node = None):
        self.data = data
        self.prev = previous_node
        self.next = next_node


