class Node:
    """二分探索木クラス"""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str({'value': self.value, 'left': self.left, 'right': self.right})


class BinarySearchTree:
    """
    # 疑似コード
    データを挿入できるまで以下の処理を繰り返す
        挿入すべき範囲に節点がある場合
            節点の方が大きければ挿入すべき範囲を左に移す
            節点の方が小さければ挿入すべき範囲を右に移す
        挿入すべき範囲に節点がない場合
            挿入したいデータの値を持つ節点を新たに作って完了
    """

    def __init__(self, root):
        self.root = Node(root)

    def insert(self, key):
        node = self.root
        while True:  # 場所が決まるまで繰り返す
            if node.value > key:
                if node.left is None:
                    node.left = Node(key)
                    return
                node = node.left  # 挿入の検討範囲を左にずらす
            elif node.value <= key:
                if node.right is None:
                    node.right = Node(key)
                    return
                node = node.right  # 挿入の検討範囲を右にずらす

    def inorder(self, node):
        if node is None:
            return
        else:
            # print(node.value)
            self.inorder(node.left)
            print(node.value)
            self.inorder(node.right)
            # print(node.value)

    def __str__(self):
        return str({'BinarySearchTree': self.root })


if __name__ == '__main__':
    print(f'{"#" * 25} Process Start {"#" * 25}')
    t = BinarySearchTree(7)
    t.insert(3)
    t.insert(9)
    t.insert(1)
    t.insert(5)
    t.inorder(t.root)
