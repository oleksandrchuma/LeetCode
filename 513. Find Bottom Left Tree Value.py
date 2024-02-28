import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
import heapq 

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def findRec(root):
            if not root:
                return (-1,-1)
            ld, lv = findRec(root.left)
            rd, rv = findRec(root.right)
            if ld >= 0 or rd >= 0:
                return (ld+1, lv) if ld >= rd else (rd+1, rv)
            return 0, root.val
        _, result = findRec(root)
        return result

start_time = time.time()
app = Solution()
root = app.findBottomLeftValue(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4))))
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

