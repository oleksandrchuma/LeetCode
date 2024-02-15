from typing import List
from typing import Optional
import time
from collections import Counter
from functools import lru_cache

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:        
        nums.sort()
        sub = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] < sub:
                res = i
            sub += nums[i]
        return sum([nums[i] for i in range(res+1)]) if res >= 2 else -1
start_time = time.time()
app = Solution()
data = [1,12,1,2,5,50,3]
root = app.largestPerimeter(data)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

