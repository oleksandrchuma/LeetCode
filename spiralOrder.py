from typing import List
from typing import Optional
import time
import math

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = []
        for _ in range(n):
            matrix.append([0]*n)
        i = 1
        top, bottom, left, right = 0, len(matrix), 0, len(matrix[0])
        res = []
        while top < bottom and left < right:
            for j in range(left, right):
                matrix[top][j] = i
                i += 1

            top += 1
            if top >= bottom:
                break

            for j in range(top, bottom):
                matrix[j][right-1] = i
                i += 1
            right -= 1

            if left >= right:
                break
            
            for j in range(right-1, left-1, -1):
                matrix[bottom-1][j] = i
                i += 1
            bottom -= 1

            if top >= bottom:
                break
            
            for j in range(bottom-1, top-1, -1):
                matrix[j][left] = i
                i += 1
            left += 1    
        return matrix


    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom, left, right = 0, len(matrix), 0, len(matrix[0])
        res = []
        while top < bottom and left < right:
            res = res + [matrix[top][j] for j in range(left, right)]
            top += 1
            if top >= bottom:
                break
            res = res + [matrix[i][right-1] for i in range(top, bottom)]
            right -= 1
            if left >= right:
                break
            res = res + [matrix[bottom-1][j] for j in range(right-1, left-1, -1)]
            bottom -= 1
            if top >= bottom:
                break
            res = res + [matrix[i][left] for i in range(bottom-1, top-1, -1)]
            left += 1    
        return res


start_time = time.time()
print(Solution().generateMatrix(4))
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
