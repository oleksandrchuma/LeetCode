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
import pprint
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        if not(node): 
            return None 
        while node.next is not None: 
            next = node.next 
            if next is None:
                break
            node.next = ListNode(math.gcd(node.val, next.val), next)
            node = next 
        return head
t = Solution()
start_time = time.time()
#root = t.removeDuplicateLetters("cbacdcbc")
root = t.insertGreatestCommonDivisors(ListNode(18, ListNode(6, ListNode(10, ListNode(3)))))
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
