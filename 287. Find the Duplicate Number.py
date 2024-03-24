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
        def search(val):
            eq = l = r = 0
            for num in nums: 
                if num == val:
                    eq += 1
                elif num < val:
                    l += 1
                else:
                    r += 1
            if eq > 1:
                return 0
            if l >= val:
                return -1
            return 1  
        left = 1
        right = len(nums)-1
        n = len(nums)-1
        while left < right: 
            mid = (left+right)//2 
            res = search(mid)
            if res == 0:
                return mid 
            elif res == -1:
                right = mid-1
            else:
                left = mid+1
        return left
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