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
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = -1
        right = -1 
        max_heap = []
        min_heap = []
        n = len(nums)
        result = 1
        while right < n-1:
            while right < n-1 and\
                (not(max_heap) or not(min_heap)
                 or (-max_heap[0][0]-nums[right+1])<=limit
                    and (nums[right+1]-min_heap[0][0])<=limit):
                right = right+1
                heapq.heappush(max_heap, (-nums[right], -right))
                heapq.heappush(min_heap, (nums[right], right)) 
            result = max(result, right-left)
            n_left = left 
            while n_left <= left: 
                if -max_heap[0][1] < min_heap[0][1]:
                    _, n_left = heapq.heappop(max_heap)
                    n_left = -n_left
                elif min_heap[0][1] < -max_heap[0][1]: 
                    _, n_left = heapq.heappop(min_heap)
                else:
                    _, n_left = heapq.heappop(min_heap)
                    heapq.heappop(max_heap)
            while max_heap and -max_heap[0][1] <= left: 
                heapq.heappop(max_heap)
            while min_heap and min_heap[0][1] <= left: 
                heapq.heappop(min_heap)
            left = n_left
        return result 

start_time = time.time()
t = Solution()
root = t.longestSubarray([24,12,71,33,5,87,10,11,3,58,2,97,97,36,32,35,15,80,24,45,38,9,22,21,33,68,22,85,35,83,92,38,59,90,42,64,61,15,4,40,50,44,54,25,34,14,33,94,66,27,78,56,3,29,3,51,19,5,93,21,58,91,65,87,55,70,29,81,89,67,58,29,68,84,4,51,87,74,42,85,81,55,8,95,39], 87)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
