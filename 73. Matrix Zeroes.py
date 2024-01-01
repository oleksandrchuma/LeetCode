from typing import List
from typing import Optional
import time
import math
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = {}
        cols = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (matrix[i][j] == 0):
                    rows[i] = 1
                    cols[j] = 1

        for x in cols.keys():
            for i in range(len(matrix)):
                matrix[i][x] = 0
        for x in rows.keys():
            for j in range(len(matrix[0])):
                matrix[x][j] = 0
        #print(matrix)
start_time = time.time()
print(Solution().setZeroes([[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]))

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

