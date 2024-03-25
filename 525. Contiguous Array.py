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
    def findMaxLength(self, nums: List[int]) -> int:
        pref_dic = {0:0}
        result = 0
        sum = 0 
        for i in range(len(nums)):
            sum += 1 if nums[i] == 1 else -1 
            if sum in pref_dic:
                result = max(i+1-pref_dic[sum], result) 
            else: 
                pref_dic[sum] = i+1         
        return result
start_time = time.time()
t = Solution()
root = t.findMaxLength([1,0,1,1,0,0])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

'''
(x+n)(n-x+1)=x(x+1) 
n2-x2+n = x2
x = sqrt((n2+n)/2)

'''