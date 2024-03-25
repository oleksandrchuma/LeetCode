import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
import math
import itertools
import heapq
from collections import Counter

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        dic = [defaultdict(list) for _ in range(k+1)]
        for j in range(1, 10-k+1):
            dic[0][j] = [[j]]
        for i in range(1, k):
            for j in range(i+1,10-k+i+1):
                for prev,combs in dic[i-1].items():
                    if prev+j <= n:
                        for l in combs:
                            if l[-1] < j:
                                dic[i][prev+j].append(l.copy() + [j])
       # print(dic)
        return dic[k-1][n]


start_time = time.time()
t = Solution()
root = t.combinationSum3(3, 7)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

'''
(x+n)(n-x+1)=x(x+1) 
n2-x2+n = x2
x = sqrt((n2+n)/2)

'''