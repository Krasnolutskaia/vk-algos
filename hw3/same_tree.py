class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


def isSameTree(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    if a.data != b.data:
        return False

    return isSameTree(a.left, b.left) and isSameTree(a.right, b.right)


if __name__ == "__main__":
    a = TreeNode(
        8,
        TreeNode(9, TreeNode(7), TreeNode(16)),
        TreeNode(11, TreeNode(3), TreeNode(1)),
    )
    b = TreeNode(
        8,
        TreeNode(9, TreeNode(7), TreeNode(16)),
        TreeNode(11, TreeNode(3), TreeNode(1)),
    )
    print(isSameTree(a, b))

    b.right.right.data = 2
    print(isSameTree(a, b))
