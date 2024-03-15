import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
import math
import heapq
from collections import Counter

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        if (len(s) != len(t)):
            return False
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = t[i]
            elif dic[s[i]] != t[i]:
                return False
        return len(dic) == len(set(dic.values()))

start_time = time.time()
app = Solution()
root = app.isIsomorphic("bbbaaaba", "aaabbbba")
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

