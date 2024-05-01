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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if (root is None):
            return []
        result = []
        stack = [root]
        while len(stack):
            next = []
            result.append([])
            for node in stack:
                result[-1].append(node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)    
            stack = next
        return result
    
start_time = time.time()
app = Solution()
print(app.levelOrder(TreeNode(1, TreeNode(2), TreeNode(3))))
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

