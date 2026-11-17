class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderMinIterative(node, k):
    stack = []
    counter = 0
    current = node

    while len(stack) > 0 or current is not None:
        while current is not None:
            stack.append(current)
            current = current.left

        current = stack.pop()
        counter += 1
        if counter == k:
            return current.val

        current = current.right

    return None


def inorderMaxIterative(node, k):
    stack = []
    counter = 0
    current = node

    while len(stack) > 0 or current is not None:
        while current is not None:
            stack.append(current)
            current = current.right

        current = stack.pop()
        counter += 1
        if counter == k:
            return current.val

        current = current.left

    return None


if __name__ == "__main__":
    root = TreeNode(
        16,
        TreeNode(
            10,
            TreeNode(6, TreeNode(2), TreeNode(8)),
            TreeNode(12, TreeNode(11), TreeNode(13)),
        ),
        TreeNode(
            22,
            TreeNode(18, TreeNode(17), TreeNode(21)),
            TreeNode(24, TreeNode(23), TreeNode(27)),
        ),
    )
    print(inorderMinIterative(root, 3))
    print(inorderMaxIterative(root, 3))
