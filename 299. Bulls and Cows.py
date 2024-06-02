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
    def getHint(self, secret: str, guess: str) -> str:
        l1 = []
        l2 = []
        a = 0
        b = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
            else: 
                l1.append(secret[i])
                l2.append(guess[i])
        counter = Counter(l1)
        for c in l2:
            if c in counter and counter[c] > 0:
                b += 1
                counter[c] -= 1
        return f"{a}A{b}B"
start_time = time.time()
t = Solution()
root = t.getHint("1123", "0111")
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
