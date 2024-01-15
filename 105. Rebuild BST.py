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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        rootval = preorder[0]
        root = TreeNode(rootval)
        split = inorder.index(rootval)
        root.left = self.buildTree(preorder[1:split+1], inorder[0:split])
        root.right = self.buildTree(preorder[split+1:], inorder[split+1:])
        return root
start_time = time.time()
app = Solution()
print(app.buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]))

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

