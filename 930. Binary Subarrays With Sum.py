import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
import math
import itertools
import heapq
from collections import Counter

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ones = [i for i,v in enumerate(nums) if v == 1]
        if len(ones) < goal: 
            return 0 
        result = 0
        
        if (goal > 0):
            for i in range(len(ones)-goal+1):
                pref = ones[i]+1 if i == 0 else ones[i]-ones[i-1]
                j = i+goal-1 
                suff = len(nums)-ones[j] if j == len(ones)-1 else ones[j+1]-ones[j]
                result += pref*suff
        else:
            prev = -1
            ones.append(len(nums))
            for i in range(len(ones)):
                result += (ones[i]-prev-1)*(ones[i]-prev)//2
                prev = ones[i] 
            
        return result
start_time = time.time()
t = Solution()
root = t.numSubarraysWithSum([0,0,0,0,0], 0)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

'''
(x+n)(n-x+1)=x(x+1) 
n2-x2+n = x2
x = sqrt((n2+n)/2)

'''