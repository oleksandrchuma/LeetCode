from typing import List
from typing import Optional
import time
import math
from collections import Counter

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        r1 = m - 1
        r2 = n - 1
    
        while r1 > -1 or r2 > -1:
            x = 0
            if r1 == -1:
                x = nums2[r2]
                r2 -= 1
            elif r2 == -1:
                x = nums1[r1]
                r1 -= 1
            elif nums1[r1] > nums2[r2]:
                x = nums1[r1]
                r1 -= 1
            else:
                x = nums2[r2]
                r2 -= 1
            nums1[r1+r2+2] = x
start_time = time.time()
nums1 = [1,2,3,0,0,0]
print(Solution().merge(nums1, 3, [2, 5, 6], 3))
print(nums1)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

