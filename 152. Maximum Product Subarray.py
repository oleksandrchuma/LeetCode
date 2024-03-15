import time
from typing import List
from collections import Counter
from functools import lru_cache

class Solution:
    def maxProductWithoutZeros(self, nums: List[int], start, end) -> int:
        if start > end:
            return 0 
        result = 1 

        for i in range(start, end+1):
            result *= nums[i]
        if (result < 0):
            first = next((i for (i, v) in enumerate(nums[start:end+1], start) if v < 0), -1)
            if first >= 0:
                if first > start:
                    result = max(result, self.maxProductWithoutZeros(nums, start, first-1))
                if first < end: 
                    result = max(result, self.maxProductWithoutZeros(nums, first+1, end))
            last = max(i for i, v in enumerate(nums[start:end+1], start) if v < 0)    
            if last != first: 
                if last > start:
                    result = max(result, self.maxProductWithoutZeros(nums, start, last-1))
                if last < end: 
                    result = max(result, self.maxProductWithoutZeros(nums, last+1, end))
            
        return result
    
    def maxProduct(self, nums: List[int]) -> int:
        result = 0
        zeros = [-1] + [i for i,x in enumerate(nums) if x == 0] + [len(nums)]
        if len(zeros) == 2:
            result = self.maxProductWithoutZeros(nums, 0, len(nums)-1)
        else: 
            for i in range(len(zeros)-1):
                result = max(self.maxProductWithoutZeros(nums, zeros[i]+1, zeros[i+1]-1), result)
                
        return result 
start_time = time.time()
app = Solution()
root = app.maxProduct([-1,-2,-3,0])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

