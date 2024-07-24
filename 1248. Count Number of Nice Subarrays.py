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
import numpy 
import pprint
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = -1
        right = -1
        n = len(nums)
        tail = 0
        head = 0
        result = 0
        while right+tail < n:
            right += tail
            while right < n-1 and k > 0:
                right += 1
                if (nums[right]%2)==1:
                    k -= 1
            if k > 0: 
                return 0
            tail = 1
            while right+tail < n and nums[right+tail]%2 == 0:
                tail += 1
            
            left += head 
            head = 1
            while left+head < n and nums[left+head]%2 == 0:
                head += 1
            result += head*tail
        return result 
start_time = time.time()
t = Solution()
root = t.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
