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
    def isAdditiveNumber(self, num: str) -> bool:
        def rec(x,y,s):
            if len(s) == 0:
                return True
            next = x+y
            s_next = str(next)
            if s.startswith(s_next):
                return rec(y,next,s[len(s_next):])
            return False
        n = len(num)
        if n < 3:
            return False
        max_len = n - n//3 + 1
        max_i = 1 if num[0] == '0' else n//2
        for i in range(max_i):
            max_j = 1 if num[i+1] == '0' else max_len-i
            for j in range(max_j):
                
                x = num[:i+1]
                y = num[i+1:i+j+2]

                if (i+j+2<n and rec(int(x),int(y),num[i+j+2:])):
                    return True 
        return False
start_time = time.time()
t = Solution()
root = t.isAdditiveNumber("199100199")
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
