import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
import math
import itertools
import heapq
from collections import Counter

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pivotInteger(self, n: int) -> int:
        x = int(math.sqrt((n*n+n)/2))
        if (x*x*2 == (n+1)*n):
            return x
        return -1
start_time = time.time()
t = Solution()
root = t.pivotInteger(4)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

'''
(x+n)(n-x+1)=x(x+1) 
n2-x2+n = x2
x = sqrt((n2+n)/2)

'''