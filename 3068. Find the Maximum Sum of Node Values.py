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
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        def log(x):
            res = 0
            y = 1
            while y*2 <= x: 
                y*=2
                res+=1
            return res      
        
        count = 0
        result = 0
        zeros = set()
        min_delta = k+1
        for i in range(len(nums)):
            xor_num = nums[i]^k
            if xor_num > nums[i]:
                zeros.add(i)
                count+=1
                result += xor_num
                if xor_num-nums[i] < min_delta:
                    min_delta = xor_num-nums[i]
            else:
                result += nums[i]
        max_delta = -k
        max_edge = (-1,-1)
        if count%2 == 1:
            for edge in edges:
                if (edge[0] in zeros)^(edge[1] in zeros):
                    delta = (nums[edge[0]]^k)-nums[edge[0]] if edge[1] in zeros else (nums[edge[1]]^k)-nums[edge[1]]
                    if delta > max_delta:
                        max_delta = delta
                        max_edge = edge
            for i in range(len(nums)):
                if i not in zeros:
                    if (nums[i]^k)-nums[i]>max_delta:
                        max_delta = (nums[i]^k)-nums[i]
            result -= min(-max_delta,min_delta)
        return result
start_time = time.time()
t = Solution()
root = t.maximumValueSum( [81,71,74,94,22,12,21,29,54,57], 7, [[3,0],[3,2],[6,4],[4,9],[8,2],[2,1],[1,5],[5,7],[9,7]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
