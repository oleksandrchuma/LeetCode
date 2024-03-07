import time
from typing import List
from collections import Counter
from functools import lru_cache

class Solution:
    def findMinRec(self, nums: List[int], start: int, end: int) -> int:
        if start == end: 
            return nums[start]
        if nums[start] < nums[end]:
            return nums[start]
        if end - start == 1:
            return nums[end]
        mid = (start+end)//2
        if nums[mid] > nums[end]:
            return self.findMinRec(nums, mid, end)
        elif nums[mid] < nums[end]:
            return self.findMinRec(nums, start, mid)
        elif nums[start] > nums[mid]:
            return self.findMinRec(nums, start, mid)
        elif nums[start] < nums[mid]:
            return self.findMinRec(nums, mid, end)
        return min(self.findMinRec(nums, mid, end), 
                   self.findMinRec(nums, start, mid))
    def findMin(self, nums: List[int]) -> int:
        return self.findMinRec(nums, 0, len(nums)-1)
start_time = time.time()
app = Solution()
root = app.findMin([5,5,5,5,5,5,5,5,5,5,4,5,5,5,5])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

