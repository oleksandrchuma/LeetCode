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
    def binarySearch(self, x, nums) -> int: 
        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] == x:
                return mid
            if nums[mid]>x:
                right = mid-1
            if nums[mid]<x:
                left = mid+1
        if left >= 0 and nums[left] > x:
            left -= 1
        return left  
    def lengthOfLIS(self, nums: List[int]) -> int:    
        lis = []
        for num in nums: 
            pos = self.binarySearch(num, lis)
            if pos >= 0 and num == lis[pos]:
                continue
            if pos+1 == len(lis):
                lis.append(num)
            else:
                lis[pos+1] = num
        return len(lis) 
start_time = time.time()
t = Solution()
root = t.lengthOfLIS([7,7,7,7,7,7,7])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
