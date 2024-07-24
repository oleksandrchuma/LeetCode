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
class Solution:
    def binarySearch(self, cp, val, low) -> int:
        left = low if low >= 0 else 0   
        right = len(cp)-1
        if cp[left][0] > val: 
            return left
        while left < right:
            mid = (left + right)//2
            if cp[mid][0] == val: 
                left = mid
                break
            if cp[mid][0] < val: 
                left = mid+1
            else:
                right = mid-1
        while left < len(cp)-1 and cp[left+1][0] <= val:
            left+=1
        if cp[left][0] > val:
            left -= 1
        return left
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        cp = sorted([(capital[i], profits[i]) for i in range(len(profits))])
        if cp[0][0]>w:
            return w
        low = -1
        heap = []
        for i in range(k):
            next = self.binarySearch(cp, w, low)
            while low < next:
                low += 1
                heapq.heappush(heap, (-cp[low][1], cp[low][0]))
            if len(heap) == 0:
                break
            p, c = heapq.heappop(heap)
            w += -p
        return w 
start_time = time.time()
t = Solution()
root = t.findMaximizedCapital(3, 0, [1,2,3], [0,1,10])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
