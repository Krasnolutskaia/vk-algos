class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


def isSymmetric(root):
    if root is None:
        return True

    queue = [root]
    while queue:
        queueLen = len(queue)
        for i in range(queueLen):
            if queue[i] is None and queue[queueLen - i - 1] is None:
                continue
            if queue[i] is None or queue[queueLen - i - 1] is None:
                return False
            if queue[i].data != queue[queueLen - i - 1].data:
                return False
            queue.append(queue[i].left)
            queue.append(queue[i].right)
        queue = queue[queueLen:]

    return True


if __name__ == "__main__":
    root = TreeNode(
        3,
        TreeNode(8, TreeNode(9), TreeNode(6)),
        TreeNode(8, TreeNode(6), TreeNode(9)),
    )
    print(isSymmetric(root))

    root = TreeNode(
        3,
        TreeNode(7, None, TreeNode(9)),
        TreeNode(8, TreeNode(6), TreeNode(9)),
    )
    print(isSymmetric(root))
