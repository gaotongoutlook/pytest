from ListNode import ListNode

if __name__ == '__main__':
    print("Hello World")

"""
    合并两个已经排序的链表
"""
def Merge(self , pHead1: ListNode, pHead2: ListNode) -> ListNode:
    if not pHead1:
        return pHead2
    if not pHead2:
        return pHead1

    dummy = ListNode(0)
    cur = dummy

    while pHead1 and pHead2:
        if pHead1.val <= pHead2.val:
            cur.next = ListNode(pHead1.val)
            pHead1 = pHead1.next
        else:
            cur.next = ListNode(pHead2.val)
            pHead2 = pHead2.next
        cur = cur.next

    while pHead1:
        cur.next = ListNode(pHead1.val)
        pHead1 = pHead1.next
        cur = cur.next

    while pHead2:
        cur.next = ListNode(pHead2.val)
        pHead2 = pHead2.next
        cur = cur.next

    return dummy.next

"""
    反转链表
"""
def ReverseList(self , head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    dummy = ListNode(0)
    pre = dummy












