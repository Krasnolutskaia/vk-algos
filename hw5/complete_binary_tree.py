"""
У полного дерева все уровни, кроме последнего, заполнены целиком.
На последнем уровне узлы стоят слева направо без пропусков.
Обходим дерево в ширину, добавляя в очередь и пустые дочерние узлы.
BFS подходит здесь, потому что проверяет узлы по уровням слева направо.
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isCompleteTree(root):
    if root is None:
        return True

    queue = deque([root])
    seenNull = False

    while len(queue) > 0:
        node = queue.popleft()
        if node is None:
            seenNull = True
        else:
            if seenNull:
                return False
            queue.append(node.left)
            queue.append(node.right)

    return True


if __name__ == "__main__":
    root = TreeNode(8, TreeNode(3, TreeNode(11), TreeNode(6)), TreeNode(9))
    print(isCompleteTree(root))

    root = TreeNode(8, TreeNode(3, None, TreeNode(6)), TreeNode(9))
    print(isCompleteTree(root))
