class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


def buildTree(arr, i):
    if i >= len(arr):
        return None

    root = TreeNode(arr[i])
    root.left = buildTree(arr, 2 * i + 1)
    root.right = buildTree(arr, 2 * i + 2)
    return root


if __name__ == "__main__":
    root = buildTree([8, 9, 11, 7, 16, 3, 1], 0)
    queue = [root]
    result = []
    while queue:
        queueLen = len(queue)
        for i in range(queueLen):
            node = queue[i]
            result.append(node.data)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        queue = queue[queueLen:]
    print(result)
