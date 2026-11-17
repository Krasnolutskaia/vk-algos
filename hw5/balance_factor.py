"""
Баланс-фактор узла в дереве рассчитывается как разница высот левого и правого поддеревьев:
balance_factor = height(left_subtree) - height(right_subtree)

Высота пустого дерева равна 0. Сначала рекурсивно вычисляем высоты детей.
Когда они известны, записываем их разность в поле balance_factor.
Высота самого узла - 1 + max(leftHeight, rightHeight). Единица учитывает текущий узел. У листа обе высоты равны 0, его высота равна 1, а баланс — 0.
Высоту каждого поддерева считаем один раз и возвращаем родителю.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.balance_factor = 0


def calculateHeightsAndBalance(node):
    if node is None:
        return 0

    leftHeight = calculateHeightsAndBalance(node.left)
    rightHeight = calculateHeightsAndBalance(node.right)
    node.balance_factor = leftHeight - rightHeight

    return 1 + max(leftHeight, rightHeight)


if __name__ == "__main__":
    root = TreeNode(
        9,
        TreeNode(3, TreeNode(16, TreeNode(21)), TreeNode(7)),
        TreeNode(8, None, TreeNode(11)),
    )
    calculateHeightsAndBalance(root)
    queue = [root]
    result = []
    for node in queue:
        result.append((node.val, node.balance_factor))
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    print(result)
