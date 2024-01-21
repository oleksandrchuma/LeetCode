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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None: 
            return []
        targetSum -= root.val 
        if targetSum == 0 and not(root.left) and not(root.right): 
            return [[root.val]] 
        ltree = self.pathSum(root.left, targetSum)
        rtree = self.pathSum(root.right, targetSum)
        result = []
        if len(ltree) > 0:
            result = result + [([root.val] + path) for path in ltree]
        if len(rtree) > 0:
            result = result + [([root.val] + path) for path in rtree] 
        return result
    
start_time = time.time()
app = Solution()
print(app.pathSum(TreeNode(1, TreeNode(7), TreeNode(3, TreeNode(4))), 8))
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

