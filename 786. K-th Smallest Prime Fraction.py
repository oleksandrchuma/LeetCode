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

class Node(object):
    def __init__(self, p: int, q:int):
        self.p = p
        self.q = q

    def __repr__(self):
        return f'{self.p}/{self.q}'

    def __lt__(self, other):

        return other.q*self.p < other.p*self.q
    
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        map = {value: index for index, value in enumerate(arr)}
        heap = []
        prev_list = []
        taken = [-1 for _ in arr]
        taken[-1] = 0
        heapq.heappush(heap, (arr[0]/arr[1], arr[0], arr[-1]))
        while k > 1:
            k -= 1
            prev = heapq.heappop(heap)
            prev_list.append(prev)
            pi = map[prev[1]]
            qi = map[prev[2]]
            if qi > pi+1:
                if qi > 1 and taken[qi-1] < pi:
                    taken[qi-1] = pi
                    heapq.heappush(heap, (prev[1]/arr[qi-1], prev[1], arr[qi-1]))
                if pi < len(arr)-1 and taken[qi] < pi+1:    
                    taken[qi] = pi+1
                    heapq.heappush(heap, (arr[pi+1]/prev[2], arr[pi+1], prev[2]))
        node = heapq.heappop(heap)

        return node[1:]
start_time = time.time()
t = Solution()
root = t.kthSmallestPrimeFraction([1,7,23,29,47],8)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
