"""
Обходим дерево в ширину. У каждого узла меняем местами ссылки на левого и правого ребёнка через temp, затем добавляем детей в очередь.
После обмена левое поддерево стоит справа, а правое - слева.
Внутри каждого из них делаем тот же обмен. 
Поэтому меняется направление каждого ребра, и всё дерево становится зеркальным, значения узлов сохраняются.

Каждый узел попадает в очередь один раз, поэтому время O(n), память O(n)
в худшем случае для очереди
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def mirrorTreeIterative(node):
    if node is None:
        return None

    queue = deque([node])

    while len(queue) > 0:
        current = queue.popleft()

        temp = current.left
        current.left = current.right
        current.right = temp

        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

    return node


if __name__ == "__main__":
    root = TreeNode(
        1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3, TreeNode(6), TreeNode(7)),
    )
    root = mirrorTreeIterative(root)
    queue = [root]
    result = []
    for node in queue:
        result.append(node.val)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    print(result)
