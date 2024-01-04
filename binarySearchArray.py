from typing import List
from typing import Optional
import time
from collections import Counter
import math
class Solution:
    def binarysearch(self, nums: List[int], target: int) -> bool:
        left = 0; right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
start_time = time.time()
print(Solution().binarysearch([0,1,2,2,5,6], 0))

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

