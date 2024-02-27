import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
import heapq 

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def diameterAndHeight(self, root):
            dl, hl = self.diameterAndHeight(root.left) if root.left else (0,0)
            dr, hr = self.diameterAndHeight(root.right) if root.right else (0,0)
            h = max(hl,hr)+1
            d = max(dl, dr, hl+hr)
            return d,h
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        d,_ = self.diameterAndHeight(root)
        return d
app = Solution()
start_time = time.time()
root = app.diameterOfBinaryTree(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3)))
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

