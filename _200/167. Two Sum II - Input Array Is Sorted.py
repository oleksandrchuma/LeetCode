import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
import heapq 
class Solution:
    def split(self, nums, x, left, right) -> int:
        while left <= right: 
            mid = (right + left) // 2
            if nums[mid] == x:
                return mid 
            elif nums[mid] < x:
                left = mid+1
            else: 
                right = mid-1
        return -1
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            x = numbers[i]
            j = self.split(numbers, target-numbers[i], i+1, len(numbers)-1)
            if j>0:
                return [i+1, j+1]
        return []
app = Solution()
start_time = time.time()
root = app.twoSum([0,0,3,4], 0)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

