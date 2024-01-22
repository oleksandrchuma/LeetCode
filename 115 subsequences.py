from typing import List
from typing import Optional
import time
import math
from collections import Counter

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        matrix = [[0 for _ in range(len(s))] for _ in range(len(t))]  
        matrix[0][0] = 1 if s[0] == t[0] else 0 
        for ti in range(0, len(t)):
            for si in range(1, len(s)):
                matrix[ti][si] += matrix[ti][si-1]
                if (t[ti] == s[si]):
                    if (ti > 0):
                        matrix[ti][si] += matrix[ti-1][si-1]
                    else: 
                        matrix[ti][si] += 1
            #print(matrix)    
        return matrix[-1][-1]             
start_time = time.time()
app = Solution()
print(app.numDistinct("rabbbit", "rabbit"))

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

