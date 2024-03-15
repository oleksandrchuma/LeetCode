from typing import List
from typing import Optional
from collections import defaultdict
import time
from collections import Counter
import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1]
        suff = [1]
        n = len(nums)
        for i in range(n-1):
            pref.append(pref[-1]*nums[i])
            suff.append(suff[-1]*nums[n-i-1])
        result = []
        for i in range(n):
            result.append(pref[i]*suff[n-i-1])
        return result 
app = Solution()
start_time = time.time()
root = app.productExceptSelf([1,2,3,4])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

