class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    dummy = ListNode()
    cur = dummy

    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
        cur = cur.next

    cur.next = list1 if list1 is not None else list2
    return dummy.next


if __name__ == "__main__":
    list1 = ListNode(3, ListNode(6, ListNode(8)))
    list2 = ListNode(4, ListNode(7, ListNode(9, ListNode(11))))
    head = mergeTwoLists(list1, list2)
    result = []
    while head is not None:
        result.append(head.val)
        head = head.next
    print(result)
