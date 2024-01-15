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
    def maxDepthLevel(self, root: Optional[TreeNode], level: int) -> int:
        if root is None: 
            return level
        return max(self.maxDepthLevel(root.left, level+1), self.maxDepthLevel(root.right, level+1))
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.maxDepthLevel(root, 0)
start_time = time.time()
app = Solution()
print(app.maxDepth(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(45, TreeNode(7))), TreeNode(3, None, TreeNode(5)))))
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

