class Node:
    """クラスで表す場合"""

    def __init__(self, value):
        self.value = value
        self.left = Node
        self.right = Node


def hoge():
    """
    # 疑似コード
    データを挿入できるまで以下の処理を繰り返す
        挿入すべき範囲に節点がある場合
            節点の方が大きければ挿入すべき範囲を左に移す
            節点の方が小さければ挿入すべき範囲を右に移す
        挿入すべき範囲に節点がない場合
            挿入したいデータの値を持つ節点を新たに作って完了
    """
    pass
