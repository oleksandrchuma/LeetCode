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
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def rec(ind, depth, l_open, l_close):
            if ind == 0:
                if l_open + l_close + depth > 0:
                    return (set(), False)
                return ({""}, True)
            if l_open+l_close+depth>ind:
                return (set(), False)
            res = set()
            h_res = False
            if s[-ind]=='(':
                sub, h = rec(ind-1, depth+1, l_open, l_close)
                if h:
                    h_res = True
                    res |= set(['('+exp for exp in sub])
                if l_open > 0:
                    sub, h = rec(ind-1, depth, l_open-1, l_close)
                    if h:
                        h_res = True
                        res |= set([exp for exp in sub])
            elif s[-ind] == ')':
                if depth > 0:
                    sub, h = rec(ind-1, depth-1, l_open, l_close)
                    if h:
                        h_res = True
                        res |= set([')'+exp for exp in sub])
                if l_close > 0:
                    sub, h = rec(ind-1, depth, l_open, l_close-1)
                    if h:
                        h_res = True
                        res |= set([exp for exp in sub])
            else:
                sub, h = rec(ind-1, depth, l_open, l_close)
                if h:
                    h_res = True
                    res |= set([s[-ind]+exp for exp in sub])
            return (res, h_res)
        s_close = 0
        s_open = 0
        for c in s:
            if c == '(':
                s_open += 1
            if c == ')':
                if s_open > 0:
                    s_open -= 1
                else: 
                    s_close += 1
        print(s_close, s_open)

        res, h = rec(len(s), 0, s_open, s_close)
        if h:
            return [exp for exp in res]
        return []
start_time = time.time()
t = Solution()
root = t.removeInvalidParentheses("(a)())()")
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
