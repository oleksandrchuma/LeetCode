import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
import heapq 
class Solution:
    def countSort(self, nums, exp):
        counts = [0]*10
        result = [0]*len(nums)
        for num in nums:
            counts[(num//exp)%10] += 1
        for i in range(1,10):
            counts[i] += counts[i-1]
        for i in range(len(nums)-1,-1,-1):
            digit = (nums[i]//exp)%10
            result[counts[digit]-1] = nums[i]
            counts[digit] -= 1
        return result
    def radixSort(self, nums):
        max_num = max(nums)
        exp = 1 
        while (max_num // exp) > 0:
            nums = self.countSort(nums, exp)
            exp *= 10
        return nums 
    def maximumGap(self, nums: List[int]) -> int:
        nums = self.radixSort(nums)
        return max([nums[i]-nums[i-1] for i in range(1, len(nums))]) if len(nums) > 1 else 0 

app = Solution()
start_time = time.time()
root = app.maximumGap([21,2,20,2,3,32,3,53,5,16,91,90,1122])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

