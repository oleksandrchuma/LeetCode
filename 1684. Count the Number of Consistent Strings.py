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
import pprint
# Definition for singly-linked list.
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allow = set(allowed)
        result = 0
        for w in words:
            if set(w).issubset(allow):
                result += 1
        return result 
t = Solution()
start_time = time.time()
#root = t.removeDuplicateLetters("cbacdcbc")
root = t.countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
