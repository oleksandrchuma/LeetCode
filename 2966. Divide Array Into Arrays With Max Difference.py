from typing import List
from typing import Optional
import time
import math
import numpy
from collections import Counter
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        if (len(nums) == 0):
            return []
        nums.sort()
        
        result =[[nums[j] for j in range(i*3, (i+1)*3)] for i in range(len(nums)//3)]
        for i in range(len(result)):
            if result[i][-1] - result[i][0] > k:
                return [] 
        return result
start_time = time.time()
app = Solution()

root = app.divideArray([1,3,3,2,7,3], 3)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
