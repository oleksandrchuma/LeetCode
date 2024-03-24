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
    def countDigitOne(self, n: int) -> int:
        k = len(str(n))
        if k == 1:
            return 1 if n >= 1 else 0
        d = int(str(n)[0])
        res = (k-1)*d*10**(k-2)
        if d > 1:
            res += 10**(k-1)
        else:
            res += int(str(n)[1:])+1
        return res + self.countDigitOne(int(str(n)[1:]))
start_time = time.time()
t = Solution()
root = t.countDigitOne(105)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

'''
(x+n)(n-x+1)=x(x+1) 
n2-x2+n = x2
x = sqrt((n2+n)/2)

'''