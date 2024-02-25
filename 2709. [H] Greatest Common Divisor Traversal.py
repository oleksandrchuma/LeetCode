import time
from typing import List
from functools import lru_cache
from collections import defaultdict
import heapq 

class Solution:
        
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        def split(x): 
            divs = []
            for prime in primes:
                if x == 1: 
                    break
                if x % prime == 0:
                    divs += [prime]
                    while x % prime == 0:
                        x //= prime
            if x > 1:
                divs.append(x)
            for div1 in divs:
                for div2 in divs:
                        graph[div1].add(div2)
                    
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317]
        n = len(nums)
        nums = [x for x in set(nums)]
        if len(nums) == 1:
            return nums[0] != 1 or n == 1
        if 1 in nums:
            return False
        
        graph = defaultdict(set)
        for num in nums: 
            split(num)
        not_visited = set(graph.keys())
        stack = [not_visited.pop()]
        while stack:
            v1 = stack.pop()            
            conn = []
            for v2 in not_visited:
                if v2 in graph[v1]:
                    conn.append(v2)
            for v in conn:
                stack.append(v)
                not_visited.remove(v)
        return len(not_visited)==0
app = Solution()
start_time = time.time()
root = app.canTraverseAllPairs([3,9,1])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

