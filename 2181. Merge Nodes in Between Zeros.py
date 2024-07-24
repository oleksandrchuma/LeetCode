import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
from queue import Queue
import math
import itertools
import heapq
from collections import Counter
import numpy 
import pprint
# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fakeHead = ListNode()
        sum = 0
        tail = fakeHead 
        while head:
            head = head.next 
            if not(head):
                break
            if head.val == 0:
                tail.next = ListNode(sum)
                tail = tail.next
                sum = 0
            else:
                sum += head.val
        return fakeHead.next
start_time = time.time()
t = Solution()
root = t.mergeNodes(ListNode(0, ListNode(3, ListNode(0, ListNode(1, ListNode(0, ListNode(2, ListNode(2, ListNode(0)))))))))
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
