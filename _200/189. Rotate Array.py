import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
from collections import Counter

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        def center():
            if nums[0] >= 0:
                return (-1,0)
            if nums[-1] < 0:
                return (len(nums)-1, len(nums))
            left, right = (0, len(nums)-1)
            while left+1<right:
                mid = (left+right)//2
                if nums[mid] >= 0:
                    right = mid
                elif nums[mid] < 0:
                    left = mid                
            return (left, right)
        n = len(nums)
        if (n == 0):
            return []
        m,p = center()
        i = 0
        res = []
        while (m >= 0 or p < n):
            if m == -1 or (p < n and abs(nums[m]) > abs(nums[p])):
                x = nums[p]
                p += 1
            else:
                x = nums[m]
                m -= 1
            res.append(x*x)
        return res
start_time = time.time()
app = Solution()
root = app.sortedSquares([])
#root = app.calculateMinimumHP([[0]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

