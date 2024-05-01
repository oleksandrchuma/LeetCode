import time
from typing import List
from functools import lru_cache

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def isPeak(k):
            return (k == 0 or nums[k]>nums[k-1]) and (k == len(nums)-1 or nums[k]>nums[k+1])
        n = len(nums)
        if n == 0:
            return -1
        if isPeak(0): 
            return 0
        if isPeak(n-1):
            return n-1
        left, right = 0, n-1
        while left < right:
            mid = (left + right)//2
            if isPeak(mid):
                return mid
            if (mid > 0 and nums[mid] < nums[mid-1]):
                right = mid - 1
            else:
                left = mid + 1      
        if left == right and isPeak(left): 
            return left
        return -1
app = Solution()
start_time = time.time()
root = app.findPeakElement([1,2,3,1])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

