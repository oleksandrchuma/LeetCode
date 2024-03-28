import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
from queue import Queue
import math
import itertools
import heapq
from collections import Counter
    # Definition for a binary tree node.
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = -1
        right = -1
        result = 0
        n = len(nums)
        dic = defaultdict(int)
        while right < n-1:
            right += 1
            dic[nums[right]]+=1
            if dic[nums[right]] > k:
                while left < right and dic[nums[right]] > k:
                    left += 1
                    dic[nums[left]] -= 1  
            elif right - left > result: 
                result = right - left
        return result
start_time = time.time()
t = Solution()
root = t.maxSubarrayLength([1,2,3,1,2,3,1,2], 2)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
