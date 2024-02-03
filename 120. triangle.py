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
class Node:
    def __init__(self, val: int = 0, left: 'Optional[Node]' = None, right: 'Optional[Node]' = None, next: 'Optional[Node]' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i-1][j] if j < len(triangle[i-1]) else triangle[i-1][j-1], 
                                      triangle[i-1][j-1] if j > 0 else triangle[i-1][j])
                
        return min(triangle[-1])
start_time = time.time()
app = Solution()
print(app.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

