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
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next:
            node.val = node.next.val
            node.next = node.next.next
start_time = time.time()
t = Solution()
root = t.deleteNode(ListNode(4))
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

'''
(x+n)(n-x+1)=x(x+1) 
n2-x2+n = x2
x = sqrt((n2+n)/2)

'''