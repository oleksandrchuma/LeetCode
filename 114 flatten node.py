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
    def flatten(self, root: Optional[TreeNode]):
        self.flattenNode(root)
        return
    
    def flattenNode(self, root: Optional[TreeNode]):
        if root is None:
            return (None, None)
        lh, lt = self.flattenNode(root.left)
        rh, rt = self.flattenNode(root.right) 
        root.left = None 
        head = root
        if lh: 
            root.right = lh 
            root = lt 
        if rh and root: 
            root.right = rh 
            root = rt 
        return (head, root)
    
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
root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
app.flatten(root)
print(app.levelOrder(root))

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

