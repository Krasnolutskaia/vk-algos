class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head):
    slow = fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


if __name__ == "__main__":
    head = None
    for val in reversed([3, 8, 9, 6, 11, 16, 17]):
        head = ListNode(val, head)
    print(middleNode(head).val)
