from typing import Any


class Node(object):

    def __init__(self, value: Any):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree(object):

    def __init__(self, node: Node = None):
        self.root = node

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
        def _search(node: Node, value) -> bool:
            if node is None:
                return False
            if node.value == value:
                return True
            elif value < node.value:
                return _search(node.left, value)
            elif value > node.value:
                return _search(node.right, value)
        return _search(self.root, value)

    def inorder(self) -> None:
        def _inorder(node: Node) -> None:
            if node is None:
                return
            _inorder(node.left)
            print(node.value)
            _inorder(node.right)
        _inorder(self.root)

    def min_value(self, node: Node) -> Node:
        current = node
        while current.left:
            current = current.left
        return current

    def remove(self, value: Any) -> Node:
        def _remove(node: Node, value: Any) -> Node:
            if node is None:
                return node
            if value < node.value:
                node.left = _remove(node.left, value)
            elif value > node.value:
                node.right = _remove(node.right, value)
            else: # value == node.value
                if node.left is None:
                    return node.right
                elif node.left is None:
                    return node.left

                temp = self.min_value(node.right)
                node.value = temp.value
                node.right = _remove(node.right, temp.value)
            return node
        return _remove(self.root, value)


if __name__ == '__main__':
    binary_tree = BinarySearchTree()
    binary_tree.insert(3)
    binary_tree.insert(6)
    binary_tree.insert(5)
    binary_tree.insert(7)
    binary_tree.insert(1)
    binary_tree.insert(10)
    binary_tree.insert(2)
    print(binary_tree.search(2))
    print(binary_tree.search(10))
    binary_tree.remove(6)
    binary_tree.inorder()






