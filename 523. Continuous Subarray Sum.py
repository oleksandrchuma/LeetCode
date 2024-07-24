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
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = defaultdict(int)
        res = 0
        dic[0] = -1
        for i in range(len(nums)):
            res = (res + nums[i])%k
            if res in dic:
                if i - dic[res] > 1:  
                    return True
            else:
                dic[res] = i
        return False
start_time = time.time()
t = Solution()
root = t.checkSubarraySum([23,2,4,6,6], 7)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
