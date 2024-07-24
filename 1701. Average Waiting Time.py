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
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                c = stack.pop()
                inner = []
                while c != '(':
                    inner.append(c)
                    c = stack.pop()
                for c in inner:
                    stack.append(c)
            else: 
                stack.append(c)
        return ''.join(stack)

start_time = time.time()
t = Solution()
root = t.reverseParentheses('(u(love)i)')
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
