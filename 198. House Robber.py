from typing import List
from typing import Optional
from collections import defaultdict
import time
import math
# Definition for singly-linked list.
class Solution:
    def rob(self, nums: List[int]) -> int:
        result = [0] * (len(nums)+1)
        result[1] = nums[0]
        for i in range(1, len(nums)):
            result[i+1] = max(result[i], result[i-1]+nums[i])
        return result[len(nums)] 
            
start_time = time.time()
app = Solution()
root = app.rob([1,2,3,1])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

