import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
import math
import itertools
import heapq
from collections import Counter

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff == 0:
            dic = {}
            for i in range(len(nums)):
                if nums[i] not in dic or i-dic[nums[i]] > indexDiff:
                    dic[nums[i]] = i 
                else: 
                    return True 
            return False        
        else:
            diffs = [-1,0,1]
            dic = defaultdict(list)
            for i in range(len(nums)):
                div = nums[i]//valueDiff
                for diff in diffs:
                    to_remove = []
                    for (val, ind) in dic[div+diff]:
                        if i - ind <= indexDiff and abs(val - nums[i]) <= valueDiff: 
                            return True 
                        elif i - ind > indexDiff: 
                            to_remove.append((val, ind))
                    for x in to_remove:
                        dic[div+diff].remove(x)
                dic[div].append((nums[i], i))
            return False
         
start_time = time.time()
t = Solution()
root = t.containsNearbyAlmostDuplicate([1,5,9,1,5,9,1,5,2], 2, 3)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

'''
(x+n)(n-x+1)=x(x+1) 
n2-x2+n = x2
x = sqrt((n2+n)/2)

'''