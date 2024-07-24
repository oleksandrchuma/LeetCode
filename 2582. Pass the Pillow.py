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
    def passThePillow(self, n: int, time: int) -> int:
        pos = time % (2*(n-1))
        return pos+1 if pos <= n-1 else (n - (pos-(n-1)))

start_time = time.time()
t = Solution()

root = t.passThePillow(4,5)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
