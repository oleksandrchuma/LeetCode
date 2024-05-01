from typing import List
from typing import Optional
import time
from collections import Counter
from functools import lru_cache

class Solution:
    def print_matrix(self, matrix):
        max_width = 2
        for row in matrix:
            print(" ".join(f"{element:>{max_width}}" for element in row))

    def reduce(self, nums: List[int], n: int) -> int:
        j = 0
        for i in range(n-1):
            if (nums[i] == nums[i+1]):
                nums[j] = nums[i]
                j += 1
        return j 
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        while n > 1:
            n = self.reduce(nums, n)
        return nums[0]             
start_time = time.time()
app = Solution()
data = [3,1,1,3,3]
root = app.majorityElement(data)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

