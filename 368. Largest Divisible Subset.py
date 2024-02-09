from typing import List
from typing import Optional
import time
import math
from collections import Counter
from functools import lru_cache

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = [[x] for x in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]%nums[j] == 0 and len(res[j]) + 1 > len(res[i]):
                    res[i] = res[j] + [nums[i]]                   
        print(res)
        return max(res, key = lambda item: len(item))
start_time = time.time()
app = Solution()
print(app.largestDivisibleSubset([343,49,8,4,2,1]))

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

