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
    # Definition for a binary tree node.
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        missing = set()
        for i in range(len(s)):
            c = s[i]
            if c in ['(', ')']:
                if c == '(':
                    stack.append((c,i))

                if c == ')':
                    if len(stack):
                         stack.pop()
                    else:
                        missing.add(i)
        while stack:
            c,i = stack.pop()
            missing.add(i)
        print(missing)
        return ''.join(s[i] for i in range(len(s)) if i not in missing)
        
start_time = time.time()
t = Solution()

root = t.minRemoveToMakeValid("lee(t(c)o)de)")
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
