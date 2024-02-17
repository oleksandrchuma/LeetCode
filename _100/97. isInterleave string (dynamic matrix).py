from typing import List
from typing import Optional
import time
import math
from collections import Counter

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if s1 == '': return s2 == s3
        if s2 == '': return s1 == s3 
        if len(s1) + len(s2) != len(s3): return False
        matrix = [[0 for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]
        matrix[0][0] = 1
        for k in range(len(s3)):
            found = False
            for i1 in range(min(k + 2, len(s1) + 1)):
                i2 = k + 1 - i1
                if (i2 < 0 or i2 > len(s2)):
                    continue
                if i1 > 0 and matrix[i2][i1-1] and s1[i1-1] == s3[k]: 
                    matrix[i2][i1] = 1
                    found = True
                if i2 > 0 and matrix[i2-1][i1] and s2[i2-1] == s3[k]: 
                    matrix[i2][i1] = 1      
                    found = True
            if not(found): 
                return False
        return matrix[len(s2)][len(s1)] == 1 
start_time = time.time()
app = Solution()
print(app.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

