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
    def countTriplets(self, arr: List[int]) -> int:
        dic = defaultdict(list)
        dic[0].append(-1)
        curr = 0
        res = 0
        for i in range(len(arr)):
            curr ^= arr[i]
            for prev in dic[curr]:
                res += i-prev-1
            dic[curr].append(i)
        return res
start_time = time.time()
t = Solution()
root = t.countTriplets([1,1,1,1,1])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
