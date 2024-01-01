from typing import List
from typing import Optional
import time
import math
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        for i in range(len(matrix)):
            for x in matrix[i]:
                if x == target:
                    return True
        return False
start_time = time.time()
print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 10))

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

