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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: 
            return False
        targetSum -= root.val 
        if targetSum == 0 and not(root.left) and not(root.right): 
            return True 
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
    
start_time = time.time()
app = Solution()
print(app.hasPathSum(TreeNode(1, None, TreeNode(3, TreeNode(4))), 1))
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

