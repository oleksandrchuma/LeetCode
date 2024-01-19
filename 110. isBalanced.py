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
    def isBalanced2(self, root):
        if root is None:
            return (0, True)
        (rh, rb) = self.isBalanced2(root.right)
        (lh, lb) = self.isBalanced2(root.left)
        result = rb and lb and abs(rh - lh) <= 1
        return max(rh, lh)+1, result

    def isBalanced(self, root: Optional[TreeNode]):
        (height, result) = self.isBalanced2(root)
        return result
    
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
    
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        result = self.inorderTraversal(root.left)
        result.append(root.val)
        result += self.inorderTraversal(root.right)
        return result
start_time = time.time()
app = Solution()
print(app.isBalanced(TreeNode(1, TreeNode(2), TreeNode(3))))
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

