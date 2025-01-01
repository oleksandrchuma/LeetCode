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
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        top = 0
        left = 0
        bottom = m-1
        right = n-1
        l = []
        while top <= bottom and left <= right: 
            for i in range(left, right+1):
                l.append((top, i))
            top += 1
            if top > bottom: 
                break
            for i in range(top, bottom+1):
                l.append((i, right))
            if left > right:
                break
            right -= 1
            for i in range(right, left-1, -1):
                l.append((bottom, i))
            if top > bottom: 
                break
            bottom -= 1
            for i in range(bottom, top-1, -1):
                l.append((i, left))
            left += 1
        result = [[-1]*n for i in range(m)]          
        for (i,j) in l:
            if not(head):
                break
            result[i][j] = head.val 
            head = head.next

        return result

t = Solution()
start_time = time.time()
#root = t.removeDuplicateLetters("cbacdcbc")
root = t.spiralMatrix(3,5, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
