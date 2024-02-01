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
    def getRow(self, rowIndex: int) -> List[int]:
        i = 1
        row = [0 for _ in range(rowIndex+1)]
        row[0] = 1
        while (i <= rowIndex+1):
            prev = 0
            for j in range(i):
                    row[j], prev = row[j] + prev, row[j]
            i += 1
        return row
start_time = time.time()
app = Solution()
print(app.getRow(4))
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

