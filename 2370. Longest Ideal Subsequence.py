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
    def longestIdealString(self, s: str, k: int) -> int:
        if len(s) <= 1:
            return len(s)
        dict = defaultdict(int)
        result = []
        for i in range(len(s)):
            v = 0
            for j in range(max(ord('a'), ord(s[i])-k), min(ord('z'), ord(s[i])+k)+1):
                if dict[j] > v:
                    v = dict[j]
            result.append(v+1)
            dict[ord(s[i])] = v+1
        return max(result)
start_time = time.time()
t = Solution()
root = t.longestIdealString("eduktdb", 15)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
