import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
import math
import heapq
from collections import Counter

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) == 0 or len(nums2) == 0:
            return -1  
        i1, i2, n1, n2 = 0, 0, len(nums1), len(nums2)
        
        while 1 == 1:
            while nums1[i1] < nums2[i2]:
                i1 += 1
                if i1 == n1:
                    return -1
            if nums1[i1] == nums2[i2]:
                return nums1[i1]
            
            while nums1[i1] > nums2[i2]:
                i2 += 1
                if i2 == n2:
                    return -1
            if nums1[i1] == nums2[i2]:
                return nums1[i1]
            
        return -1
start_time = time.time()
app = Solution()
root = app.getCommon(nums1 = [1,2,3,6], nums2 = [0,4,4,5])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

