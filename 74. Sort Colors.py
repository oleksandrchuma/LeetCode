from typing import List
from typing import Optional
import time
import math
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        pos = [-1] * 3
        for i in range(len(nums)):
            x = nums[i]
            ins = -1
            for j in range(x, -1, -1):
                if (pos[j] != -1):
                    ins = pos[j]
                    break
            ins += 1 
            nums[ins] = x
            pos[x] = ins
            for j in range(x+1, 3):
                if pos[j] > -1:
                    pos[j] += 1
                    nums[pos[j]] = j
        print(nums)
start_time = time.time()
print(Solution().sortColors([2,0,2,1,1,0]))

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

