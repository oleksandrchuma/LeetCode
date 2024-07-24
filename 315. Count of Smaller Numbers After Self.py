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
    def countSmaller(self, nums: List[int]) -> List[int]:
        def pos(x):
            if len(arr) == 0:
                return -1
            left = 0
            right = len(arr)-1
            while left < right:
                mid = (left+right)//2
                if x <= arr[mid] and (mid == 0 or x > arr[mid-1]):
                    return mid-1
                elif x > arr[mid]:
                    left = mid+1
                else: 
                    right = mid-1
            if x <= arr[left]:
                left -= 1
            return left
        arr = []
        res = []
        for i in range(len(nums)-1, -1, -1):
            p = pos(nums[i])
            res.append(p+1)
            arr.insert(p+1, nums[i])
        return list(reversed(res))
start_time = time.time()
t = Solution()
root = t.countSmaller([-1, -1])

print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
