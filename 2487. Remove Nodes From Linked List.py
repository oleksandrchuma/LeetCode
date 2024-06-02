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
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not(head):
            return None
        fakeHead = ListNode(100001, head)
        node = head
        stack = [fakeHead]
        while node.next:
            if node.next.val > node.val:
                next = node.next
                node = stack.pop()
                node.next = next
            else:
                stack.append(node)
                node = node.next
        return fakeHead.next
    def print(self, head: Optional[ListNode]):
        while head:
            print(head.val, end='')
            head = head.next
            print('=>', end='')
        print('None')        
start_time = time.time()
t = Solution()
root = t.removeNodes(ListNode(5, ListNode(2, ListNode(13, ListNode(3, ListNode(8))))))
t.print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
