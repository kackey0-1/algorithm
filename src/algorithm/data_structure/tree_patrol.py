"""
# 木の巡回

## 中間順巡回:
    左部分技、根節点、右部分技の順に節点を巡回して出力する方法(=再帰的なアルゴリズム)
    二分探索木を中間順巡回すると昇順に出力される
# 二分探索木による探索
# 二分探索木からの削除
    子を持たない場合:
    子を1つもつ場合: 節点を探索し、削除してその子を節点に設定する
    子を2つもつ場合: 節点を探索し、削除する。右の子を節点に設定する。

"""


def inoder(node):
    pass


class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree():
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, value):
        node = self.root
        while True:
            if node.value > value:
                if node.left is None:
                    node.left = Node(value)
                    return
                node = node.left
            elif node.value <= value:
                if node.right is None:
                    node.right = Node(value)
                    return
                node = node.right

    def inorder(self, node):
        """擬似コード
                1. 左の部分技をinoderで中間順巡回する
                2. ルートを出力する
                3. 右の部分技をinoderで中間順巡回する
        :param node:
        :return:
        """
        if node is None:
            return
        else:
            self.inorder(node.left)
            print(node.value)
            self.inorder(node.right)

    def search(self, key):
        """擬似コード
                - データを探索できるまで以下の処理を繰り返す
                - 節点と探索するデータを比較する
                    - 節点と等しければ「yes」と出力して処理を終了
                    - 節点のほうが大きければ探索範囲を左に移す
                    - 節点のほうが小さければ探索範囲を右に移す
                - 探索範囲に節点がなければ「no」と出力して探索を終了する
        :param key:
        :return:
        """
        node = self.root
        while True:
            if node is None:
                print("NO")
                return None
            elif node.value == key:
                print("YES")
                return node
            elif node.value > key:
                node = node.left
            else:
                node = node.right

    def delete(self, key):
        """
            探索を行い、削除対象の節点を見つける
            削除対象の節点の子が0個の場合
                削除対象の節点を削除する
            削除対象の節点の子が1この場合
                削除対象の場所を、削除対象の節点の部分技で置き換える
            削除対象の節点の子が2この場合
                削除対象の節点の右の部分技の最小値mを削除して、削除対象の節点をmで上書きする
        :param key:
        :return:
        """
        node = self.search(key)
        if node.left is None & node.right is None:
            node = None
        elif (node.left or node.right) and not (node.left and node.right):
            if node.left:
                node = node.left
            else:
                node = node.right
        else:
            self.search()
        pass


if __name__ == '__main__':
    t = BinarySearchTree(7)
    t.insert(3)
    t.insert(19)
    # print(t.root.value, t.root.left.value, t.root.right.value)
    t.inorder(t.root)
    t.search(19)
