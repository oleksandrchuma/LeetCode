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
    def appendCharacters(self, s: str, t: str)->int:
        res = 0
        dic = defaultdict(list)
        for i in range(len(t)):
            dic[t[i]].append(i)
        for c in s: 
            if len(dic[c]) > 0 and dic[c][0] == res:
                res += 1
                dic[c].pop(0)
        return len(t)-res
start_time = time.time()
t = Solution()
root = t.appendCharacters('coaching','coding')
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
