from typing import Any


class Node(object):
    def __init__(self, value: Any) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree(object):

    def __init__(self) -> None:
        self.root = None

    def insert(self, value: Any):
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

    def inorder(self) -> None:
        def _inorder(node: Node) -> None:
            if node is not None:
                _inorder(node.left)
                print(node.value)
                _inorder(node.right)
        _inorder(self.root)

    def search(self, value: Any) -> bool:
        def _search(node: Node, value: Any) -> bool:
            if node is Node:
                return False
            if node.value == value:
                return True
            elif node.value > value:
                return _search(node.left, value)
            elif node.value < value:
                return _search(node.right, value)
        return _search(self.root, value)

    def min_value(self, node: Node) -> Node:
        current = node
        while current.left is not None:
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
            else:  # value == node.value
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left

                temp = self.min_value(node.right)
                node.value = temp.value
                node.right = _remove(node.right, temp.value)
            return node
        return _remove(self.root, value)


def insert(node: Node, value: int) -> Node:
    if node is None:
        return Node(value)

    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node


def inorder(node: Node) -> None:
    # Inorder: Left, Root, Right
    # Preorder: Root, Left, Right
    # Postorder: Left, Right, Root
    if node is not None:
        inorder(node.left)
        print(node.value)
        inorder(node.right)


def search(node: Node, value: Any) -> bool:
    if node is None:
        return False

    if node.value == value:
        return True
    elif node.value > value:
        return search(node.left, value)
    elif node.value < value:
        return search(node.right, value)


def min_value(node: Node) -> Node:
    current = node
    while current.left is not None:
        current = current.left
    return current


def remove(node: Node, value: Any) -> Node:
    if node is None:
        return node

    if value < node.value:
        node.left = remove(node.left, value)
    elif value > node.value:
        node.right = remove(node.right, value)
    else:  # value == node.value
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left

        temp = min_value(node.right)
        node.value = temp.value
        node.right = remove(node.right, temp.value)
    return node


if __name__ == '__main__':
    # root = None
    # root = insert(root, 3)
    # root = insert(root, 6)
    # root = insert(root, 5)
    # root = insert(root, 7)
    # root = insert(root, 1)
    # root = insert(root, 10)
    # root = insert(root, 2)
    # print(root.left.right.value)
    # print(root.right.value)
    # print(root.right.left.value)
    # root = remove(root, 6)
    # inorder(root)
    # print(search(root, 4))
    binary_tree = BinarySearchTree()
    binary_tree.insert(3)
    binary_tree.insert(6)
    binary_tree.insert(5)
    binary_tree.insert(7)
    binary_tree.insert(1)
    binary_tree.insert(10)
    binary_tree.insert(2)
    print(binary_tree.search(2))
    binary_tree.remove(6)
    binary_tree.inorder()



