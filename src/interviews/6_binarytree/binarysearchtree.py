from typing import Any


class Node(object):

    def __init__(self, value: Any):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree(object):

    def __init__(self) -> None:
        self.root = None

    def insert(self, value: Any) -> None:
        if self.root is None:
            self.root = Node(value)
            return

        def _insert(node: Node, value: Any) -> Node:
            if node is None:
                return Node(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node
        _insert(self.root, value)

    def search(self, value: Any) -> bool:
        def _search(node: Node, value: Any) -> bool:
            if node is None:
                return False
            if value < node.value:
                return _search(node.left, value)
            elif value > node.value:
                return _search(node.right, value)
            else:
                return True
        return _search(self.root, value)

    def inorder(self) -> None:
        def _inorder(node: Node) -> None:
            if node:
                _inorder(node.left)
                print(node.value)
                _inorder(node.right)
        _inorder(self.root)

    def remove(self) -> None:

        pass


if __name__ == '__main__':
    b = BinarySearchTree()
    b.insert(10)
    b.insert(2)
    b.insert(100)
    b.insert(1)
    b.insert(3)
    print(b.search(3))
    b.inorder()






