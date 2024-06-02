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
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fakeHead = ListNode(0, head)
        node = fakeHead
        while node.next:
            dv = node.next.val*2
            node.next.val = dv%10
            node.val = node.val + dv//10
            node = node.next
        return fakeHead if fakeHead.val > 0 else fakeHead.next
    
    def print(self, head: Optional[ListNode]):
        while head:
            print(head.val, end='')
            head = head.next
            print('=>', end='')
        print('None')        
start_time = time.time()
t = Solution()
root = t.doubleIt(ListNode(9, ListNode(9, ListNode(9))))
t.print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
