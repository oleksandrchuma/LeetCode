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

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = finder = len(nums) - 1
        while True:
            slow = nums[slow]-1
            fast = nums[nums[fast]-1]-1
            if slow == fast:
                break
        while True:
            finder = nums[finder]-1
            slow = nums[slow]-1
            if slow == finder:
                break 
        return slow+1
start_time = time.time()
t = Solution()
root = t.findDuplicate([7,9,7,4,2,8,7,7,1,5])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

'''
(x+n)(n-x+1)=x(x+1) 
n2-x2+n = x2
x = sqrt((n2+n)/2)

'''