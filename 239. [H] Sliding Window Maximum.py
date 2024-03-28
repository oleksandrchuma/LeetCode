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
    def getSkyline(self, buildings: List[List[int]], base: int) -> List[List[int]]:
        def add_res(l, h):
            if len(res)== 0 or res[-1][0] < l:
                res.append([l,h])
            else: 
                res[-1][1] = max(res[-1][1], h)
        lower = []
        i = 0
        m_h = base
        m_right = math.pow(2, 31)
        res = []
        while i < len(buildings) or len(lower) > 0:
            while i < len(buildings) and buildings[i][0] <= m_right:    
                c_left, c_right, c_h = buildings[i]
                i+=1
                if c_h == m_h:
                    m_right = max(m_right, c_right)
                elif c_h < m_h:
                    if c_right > m_right:
                        heapq.heappush(lower, (-c_h, m_right, c_right))
                elif c_h > m_h:
                    if c_right < m_right:
                        heapq.heappush(lower, (-m_h, c_right, m_right))
                    m_right = c_right 
                    m_h = c_h 
                    add_res(c_left, m_h)

            while len(lower) > 0:
                c_h, c_left, c_right = heapq.heappop(lower)
                c_h = -c_h
                if c_right > m_right:
                    if c_h < m_h:
                        add_res(m_right, c_h)
                    m_h = c_h 
                    m_right = c_right
                    break
        return res
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        buildings = [] 
        base = nums[0]
        for i in range(len(nums)):
            buildings.append([max(0, i-k+1), min(i+1, len(nums)), nums[i]])
            if base > nums[i]:
                base = nums[i]
        skyline = self.getSkyline(buildings, base)
       # print(buildings)
        result = []
        for i in range(len(skyline)-1):
            result += [skyline[i][1]]*(skyline[i+1][0]-skyline[i][0])
        
        return result[0:len(nums)-k+1]
start_time = time.time()
t = Solution()
root = t.maxSlidingWindow([1,3,1,2,0,5], 3)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
