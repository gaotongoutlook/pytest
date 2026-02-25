from typing import List
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

    pre = None
    cur = head

    while cur:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next

    return pre

"""
    链表内指定区间反转
"""
def reverseBetween(self , head: ListNode, m: int, n: int) -> ListNode:
    if not head:
        return None
    if m==n:
        return head

    count = 1
    pre = None
    cur = head
    while count<m:
        pre = cur
        cur = cur.next
        count += 1



    return None

"""
    合并K个已升序的链表
"""
def mergeKLists(self , lists: List[ListNode]) -> ListNode:
    if not lists:
        return None
    if len(lists)==1:
        return lists[0]
    return self.merge(lists, 0, len(lists)-1)

def merge(self, lists, start, end) -> ListNode:
    if start==end:
        return lists[start]

    mid = start + (end-start)>>1
    leftResult = self.merge(lists, start, mid)
    rightResult = self.merge(lists, mid+1, end)

    dummy = ListNode(0)
    cur = dummy
    while leftResult and rightResult:
        if leftResult.val <= rightResult.val:
            cur.next = leftResult
            leftResult = leftResult.next
        else:
            cur.next = rightResult
            rightResult = rightResult.next
        cur = cur.next

    cur.next = leftResult if leftResult else rightResult

    return dummy.next

"""
    链表中的节点每k个一组翻转
"""
def reverseKGroup(self , head: ListNode, k: int) -> ListNode:

    return None

"""
    单链表的排序 归并排序
"""
def sortInList(self , head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    slow = head
    fast = head.next # 链表的中间节点 此处要好好学习
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None

    left = self.sortInList(head)
    right = self.sortInList(mid)

    return self.mergeSortInList(left, right)

def mergeSortInList(left: ListNode, right: ListNode) -> ListNode:
    dummy = ListNode(0)
    cur = dummy

    while left and right:
        if left.val <= right.val:
            cur.next = left
            left = left.next
        else:
            cur.next = right
            right = right.next
        cur = cur.next

    cur.next = left if left else right

    return dummy.next

"""
    两个链表的第一个公共节点
"""
def FindFirstCommonNode(self , pHead1 , pHead2 ):
    if not pHead1 or not pHead2:
        return None

    n = 1
    cur = pHead1
    while cur:
        n += 1
        cur = cur.next

    m = 1
    cur = pHead2
    while cur:
        m += 1
        cur = cur.next

    cur1 = pHead1
    cur2 = pHead2
    if n > m:
        while n>m:
            n -= 1
            cur1 = cur1.next
    elif n < m:
        while n<m:
            m -= 1
            cur2 = cur2.next

    while cur1.val != cur2.val:
        cur1 = cur1.next
        cur2 = cur2.next

    return cur1

"""
    链表中环的入口结点
"""
def EntryNodeOfLoop(self, pHead):
    if not pHead:
        return pHead

    slow = pHead
    fast = pHead
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            fast = pHead
            while fast != slow:
                slow = slow.next
                fast = fast.next
            return slow

    return None
















