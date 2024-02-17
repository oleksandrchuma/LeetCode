from typing import List
from typing import Optional
import time
import math
class Solution:
    def solveRow(self, row: int, n:int, solution: List[int], all: List[List[int]]):
        if (row == n):
            all.append(solution)
        exclude = set()
        if (row > 0):
            exclude = set(solution[i] + (row-i) for i in range(row))\
                .union(set(solution[i] - (row-i) for i in range(row)))\
                .union(solution) 
        for i in range(n):
            if (i not in exclude):
                self.solveRow(row+1, n, solution[:] + [i], all)
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        print(self.solveRow(0, n, [], res))
        strRes = []
        for pos in res:
            posStr = []
            for line in pos:
                posStr.append("".join(["."]*line+["Q"]+["."]*(n-line-1)))
            strRes.append(posStr)    
        return strRes
    def totalNQueens(self, n: int) -> int:
        return len(self.solveNQueens(n))
    
start_time = time.time()
print(Solution().solveNQueens(2))
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
