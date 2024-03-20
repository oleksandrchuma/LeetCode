import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
import math
import itertools
import heapq
from collections import Counter

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        def nthParent(head, n):
            i = 0
            node = head
            while i < n:
                node = node.next
                i += 1
            return node
        def tail(head):
            while head and head.next:
                head = head.next
            return head 
        fake = ListNode()
        fake.next = list1
        aparent = nthParent(fake, a)
        bparent = nthParent(fake, b+1)
        list2tail = tail(list2)
        if not(aparent) or not(bparent):
            return ListNode(-1)
        if list2:
            aparent.next = list2 
            tail(list2).next = bparent.next
        else:
            aparent.next = bparent.next
        return fake.next
    def printList(self, head):
        while (head):
            print(head.val, end="=>")
            head = head.next
        print("None")
start_time = time.time()
t = Solution()
root = t.mergeInBetween(ListNode(10, ListNode(1, ListNode(13, ListNode(6, ListNode(9, ListNode(5)))))), 0, 5, ListNode(1))
t.printList(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

'''
(x+n)(n-x+1)=x(x+1) 
n2-x2+n = x2
x = sqrt((n2+n)/2)

'''