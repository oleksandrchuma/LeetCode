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
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        words = s.split()
        if (len(words) != len(pattern)):
            return False
        for i in range(len(words)):
            if words[i] not in dic: 
                dic[words[i]] = pattern[i]
            elif dic[words[i]] != pattern[i]:
                return False
        return len(dic) == len(set(dic.values()))
start_time = time.time()
t = Solution()
root = t.wordPattern("abba", "dog cat cat dog")
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
