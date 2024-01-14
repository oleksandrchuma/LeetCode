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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if (root is None):
            return []
        result = []
        stack = [root]
        dir = 1
        while len(stack):
            next = []
            result.append([])
            while len(stack):
                node = stack.pop()
                result[-1].append(node.val)
                if dir == 1 and node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)    
                if dir == -1 and node.left:
                    next.append(node.left)
            stack = next
            dir *= -1
        return result
    
start_time = time.time()
app = Solution()
print(app.zigzagLevelOrder(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(45)), TreeNode(3, None, TreeNode(5)))))
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

