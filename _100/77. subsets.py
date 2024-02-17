from typing import List
from typing import Optional
import time
from collections import Counter
import math
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        k = len(nums)
        n = len(nums)
        rez = []
        v = []
        stack = []
        stack.append(v)
        while (len(stack)):
            v = stack.pop(0)
            rez.append(v)
            for i in range(0 if len(v) == 0 else nums.index(v[-1]) + 1, n):
                x = v + [nums[i]] 
                if (len(x) == k):
                    rez.append(x)
                else:
                    stack.append(x)

        return rez 
start_time = time.time()
print(Solution().subsets([1, 2, 3]))

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

