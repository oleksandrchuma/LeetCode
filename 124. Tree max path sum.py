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
    maxVal = None
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath(root)
        return 0 if self.maxVal is None else self.maxVal
    def maxPath(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0 
        l = self.maxPath(root.left)
        r = self.maxPath(root.right)
        s = root.val + max(l + r, max(l, r), 0)
        if (self.maxVal is None or self.maxVal < s):
            self.maxVal = s
        res =  root.val + max(l, r, 0)
        return res
    
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
    
    def build(self, nodes: List[int]) -> Optional[TreeNode]:    
        if (len(nodes) == 0 or nodes[0] is None):
            return None
        root = TreeNode(nodes[0])
        queue = []
        queue.append(root)
        i = 1
        while i < len(nodes):
            node = queue.pop()
            if nodes[i] is not None:
                node.left = TreeNode(nodes[i])    
                queue.insert(0, node.left)
            i+=1
            if i >= len(nodes):
                    break
            if nodes[i] is not None:
                node.right = TreeNode(nodes[i])
                queue.insert(0, node.right)
            i+=1
        return root    
start_time = time.time()
app = Solution()
root = app.build([9,6,-3,None,None,-6,2,None,None,2,None,-6,-6,-6])
print(app.levelOrder(root))
print(app.maxPathSum(root))
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

