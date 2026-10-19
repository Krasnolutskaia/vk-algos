class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head, val):
    dummy = ListNode()
    dummy.next = head
    prev = dummy
    cur = head

    while cur is not None:
        if cur.val == val:
            prev.next = cur.next
        else:
            prev = cur
        cur = cur.next

    return dummy.next


if __name__ == "__main__":
    for val in [3, 1]:
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        head = removeElements(head, val)
        result = []
        while head is not None:
            result.append(head.val)
            head = head.next
        print(result)
