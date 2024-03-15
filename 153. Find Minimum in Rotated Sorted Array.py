import time
from typing import List
from collections import Counter
from functools import lru_cache

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]
        left, right = 0, len(nums)-1
        while right-left > 1:
            mid = (right + left) // 2
            if nums[mid] < nums[left]:
                right = mid
            else:
                left = mid
        return nums[right]
start_time = time.time()
app = Solution()
root = app.findMin([3,4,5,1,2])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

