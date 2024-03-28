from typing import List
from typing import Optional
from collections import defaultdict
import time
from collections import Counter
import math
import hashlib
 
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
     
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums = self.radixSort(nums)
        res = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]: 
                res.append(nums[i])
        return res
start_time = time.time()
app = Solution()
root = app.findDuplicates([4,3,2,7,8,2,3,1])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")


