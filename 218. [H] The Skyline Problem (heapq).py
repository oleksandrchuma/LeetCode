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
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        def add_res(l, h):
            if len(res)== 0 or res[-1][0] < l:
                res.append([l,h])
            else: 
                res[-1][1] = max(res[-1][1], h)
        lower = []
        i = 0
        m_h = 0
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
    
start_time = time.time()
t = Solution()
root = t.getSkyline([[1,38,219],[2,19,228],[2,64,106],[3,80,65],[3,84,8],[4,12,8],[4,25,14],[4,46,225],[4,67,187],[5,36,118],[5,48,211],[5,55,97],[6,42,92],[6,56,188],[7,37,42],[7,49,78],[7,84,163],[8,44,212],[9,42,125],[9,85,200],[9,100,74],[10,13,58],[11,30,179],[12,32,215],[12,33,161],[12,61,198],[13,38,48],[13,65,222],[14,22,1],[15,70,222],[16,19,196],[16,24,142],[16,25,176],[16,57,114],[18,45,1],[19,79,149],[20,33,53],[21,29,41],[23,77,43],[24,41,75],[24,94,20],[27,63,2],[31,69,58],[31,88,123],[31,88,146],[33,61,27],[35,62,190],[35,81,116],[37,97,81],[38,78,99],[39,51,125],[39,98,144],[40,95,4],[45,89,229],[47,49,10],[47,99,152],[48,67,69],[48,72,1],[49,73,204],[49,77,117],[50,61,174],[50,76,147],[52,64,4],[52,89,84],[54,70,201],[57,76,47],[58,61,215],[58,98,57],[61,95,190],[66,71,34],[66,99,53],[67,74,9],[68,97,175],[70,88,131],[74,77,155],[74,99,145],[76,88,26],[82,87,40],[83,84,132],[88,99,99]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

'''
(x+n)(n-x+1)=x(x+1) 
n2-x2+n = x2
x = sqrt((n2+n)/2)

'''