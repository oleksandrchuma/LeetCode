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
    def minDifference(self, arr: List[int]) -> int:
        if len(arr) <= 4:
            return 0
        min_q = []
        max_q = []
        for num in arr: 
            if len(min_q) < 4 or num < min_q[-1]:
                i = 0
                while i < len(min_q) and min_q[i] < num:
                    i+=1
                min_q.insert(i, num)
                if len(min_q) > 4:
                    min_q.pop(-1)
            if len(max_q) < 4 or num > max_q[0]:
                i = 0
                while i < len(max_q) and max_q[i] < num:
                    i+=1
                max_q.insert(i, num)
                if len(max_q) > 4:
                    max_q.pop(0)
            
        return min([max_q[i]-min_q[i] for i in range(4)])

start_time = time.time()
t = Solution()
root = t.minDifference([1,5,0,8,8,10,14])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
