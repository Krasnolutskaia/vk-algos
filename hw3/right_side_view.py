class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


def rightSideViewBFS(root):
    if root is None:
        return []

    queue = [root]
    result = []
    while queue:
        size = len(queue)
        i = 0
        while i < size:
            node = queue[i]
            if i == size - 1:
                result.append(node.data)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            i += 1
        queue = queue[size:]

    return result


if __name__ == "__main__":
    root = TreeNode(
        16,
        TreeNode(8, None, TreeNode(11, TreeNode(18))),
        TreeNode(9, None, TreeNode(12)),
    )
    print(rightSideViewBFS(root))
