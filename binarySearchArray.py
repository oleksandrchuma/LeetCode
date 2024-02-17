from typing import List
from typing import Optional
import time
from collections import Counter
import math
class Solution:

    def binarySearch(self, nums: List[int], target: int, left: int, right: int) -> bool:
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
    
    def search(self, nums: List[int], target: int) -> bool:
        return self.search2(nums, target, 0, len(nums)-1)
    
    def search2(self, nums: List[int], target: int, left: int, right: int) -> bool:
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] == nums[left] and nums[right] == nums[mid]:
                return self.search2(nums, target, left, mid - 1) or self.search2(nums, target, mid + 1, right) 
            elif nums[mid] > target:
                if nums[left] <= target or nums[right] >= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[right] >= target or nums[left] <= nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return (left < len(nums) and nums[left] == target)\
            or (right > 0 and nums[right] == target) 
start_time = time.time()
print(Solution().search([2,2,2,2,-1,0], 2))

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

