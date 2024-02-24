import time
from typing import List
from functools import lru_cache
import heapq 

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        dic = {}
        for m in meetings:
            x, y, t = m[0], m[1], m[2]
            if t not in dic: 
                dic[t] = [set([x,y])]
            elif len(dic[t]) == 1: 
                if x in dic[t][0]:
                    dic[t][0].add(y)
                elif y in dic[t][0]:
                    dic[t][0].add(x)
                else:
                    dic[t].append(set([x,y]))
            else:
                i = 0
                pair = set([x,y])
                while i < len(dic[t]):
                    s = dic[t][i]
                    if x in s or y in s:
                        pair |= s
                        dic[t].pop(i)
                    else:
                        i+=1
                dic[t] += [pair]
        heap = list(dic.items())
        heapq.heapify(heap)
        res = set([0, firstPerson])
        while (heap):
            _, setList = heapq.heappop(heap)
            for s in setList:
                if res & s:
                    res |= s    
        return list(res)
app = Solution()
start_time = time.time()
root = app.findAllPeople(4, [[3,1,3],[1,2,2],[0,3,3]], 3)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

