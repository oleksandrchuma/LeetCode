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
    # Definition for a binary tree node.
class Solution:
    def countInterval(self, nums: List[int], minK: int, maxK: int) -> int:
        if minK == maxK: 
            return len(nums)*(len(nums)+1)//2
        limit = -1
        pos = -1
        bases = []
        result = 0
        print(nums)
        for i in range(len(nums)):
            if nums[i] == minK or nums[i] == maxK:
                if limit == nums[i]:
                    pos = i
                else:
                    if limit != -1:
                        bases.append((pos,i))
                    limit = nums[i]
                    pos = i
        print(bases)
        for i in range(len(bases)):
            head = bases[i][0]+1 if i == 0 else bases[i][0]-bases[i-1][0]
            tail = len(nums)-bases[i][1]
            result += head*tail
            #print(head, tail)
        return result
        
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        intervals = []
        n = len(nums)
        i = 0
        while i < n:
            while i < n and (nums[i] > maxK or nums[i] < minK):              
                i+=1
            start = i 
            while i < n and (nums[i] <= maxK and nums[i]>= minK):
                i+=1
            end = i 
            if start < n: 
                intervals.append(nums[start:end])
        return sum(self.countInterval(interval, minK, maxK) for interval in intervals)
start_time = time.time()
t = Solution()

root = t.countSubarrays([35054,398719,945315,945315,820417,945315,35054,945315,171832,945315,35054,109750,790964,441974,552913], 35054, 945315)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
