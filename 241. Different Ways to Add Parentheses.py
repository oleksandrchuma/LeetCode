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
    def diffWaysToCompute(self, expression: str) -> List[int]:
        pos = 0
        n = len(expression)
        digits = []
        ops = []
        while pos < n:
            dlen = 0
            while pos+dlen < n and expression[pos+dlen].isnumeric():
                dlen += 1
            digits.append(int(expression[pos:pos+dlen]))
            pos += dlen 
            if pos < n:
                ops.append(expression[pos:pos+1])
                pos += 1
        combs = [[[] for _ in range(len(digits))] for _ in range(len(digits))]
        for i in range(len(digits)):
            combs[i][i] = [digits[i]]
        for k in range(1, len(digits)):
            for i in range(len(digits)-k):
                variants = []
                for j in range(k):
                    operation = ops[i+j]
                    left = combs[i][i+j]
                    right = combs[i+j+1][i+k]
                    for x in left: 
                        for y in right: 
                            if operation == '*':
                                variants.append(x*y)
                            elif operation == '+':
                                variants.append(x+y)
                            elif operation == '-':
                                variants.append(x-y)
                combs[i][i+k] = variants
        #print(combs)
        return combs[0][-1]
start_time = time.time()
t = Solution()

root = t.diffWaysToCompute("2*3-4*5")
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
