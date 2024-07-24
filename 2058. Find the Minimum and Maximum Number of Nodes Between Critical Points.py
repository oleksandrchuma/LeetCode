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
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:        
        first,prev,min_dist = (-1,-1,-1)
        dir = 0
        pos = 0
        while head and head.next:
            next_dir = 1 if head.next.val > head.val else (-1 if head.next.val < head.val else 0)
            if next_dir * dir == -1:
                if first == -1:
                    first = pos 
                if prev != -1 and ((pos-prev) < min_dist or min_dist == -1):
                    min_dist = pos-prev
                prev = pos 

            dir = next_dir
            head = head.next
            pos += 1
        return [min_dist, prev-first] if first > 0 and prev > first else [-1, -1]
start_time = time.time()
t = Solution()

root = t.nodesBetweenCriticalPoints(ListNode(5, ListNode(3, ListNode(1, ListNode(2, ListNode(5, ListNode(1, ListNode(2))))))))
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
