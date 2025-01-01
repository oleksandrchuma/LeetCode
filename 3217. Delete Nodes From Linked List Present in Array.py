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
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        num_set = set(nums)
        fakehead = ListNode(0, head)
        node = fakehead
        while (node.next):
            if node.next.val in num_set:
                node.next = node.next.next 
            else: 
                node = node.next
        return fakehead.next

t = Solution()
start_time = time.time()
#root = t.removeDuplicateLetters("cbacdcbc")
root = t.modifiedList([1,2,3], ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
print(root.val)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
