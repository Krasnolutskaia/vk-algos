class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head):
    if head is None or head.next is None:
        return False

    slow = head
    fast = head.next

    while slow is not fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next

    return True


if __name__ == "__main__":
    nodes = [ListNode(val) for val in [11, 3, 8, 9, 6, 11, 16, 17]]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    nodes[-1].next = nodes[2]
    print(hasCycle(nodes[0]))

    nodes[-1].next = None
    print(hasCycle(nodes[0]))
