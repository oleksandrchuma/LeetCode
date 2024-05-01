import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
import math
import heapq

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        def move(hp: tuple, delta: int) -> tuple:
            if (delta >= 0):
                return (max(hp[0]-delta, 1), max(hp[1]-delta, 1))
            return (hp[0]+abs(delta), max(hp[1], hp[0]+abs(delta))) 
        n = len(dungeon)
        m = len(dungeon[0])
        res = [[(0,0) for _ in range(m)] for _ in range(n)]
        
        res[-1][-1] = move((1,1), dungeon[-1][-1])
        for row in range(n-1,-1,-1):
            for col in range(m-1,-1,-1):
                if (row < n-1 or col < m-1):
                    if row == n-1:
                        res[row][col] = move(res[row][col+1], dungeon[row][col])
                    elif col == m-1:
                        res[row][col] = move(res[row+1][col], dungeon[row][col])
                    else:
                        op1 = move(res[row][col+1], dungeon[row][col])        
                        op2 = move(res[row+1][col], dungeon[row][col])
                        if (op1[1] > op2[1]):
                            res[row][col] = op2
                        elif (op1[1] < op2[1]):
                            res[row][col] = op1
                        else: 
                            res[row][col] = (min(op1[0],op2[0]), op1[1])
        print(res)
        return res[0][0][1]
start_time = time.time()
app = Solution()
root = app.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]])
#root = app.calculateMinimumHP([[0]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

