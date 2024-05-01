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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(postorder) == 0:
            return None
        rootval = postorder[-1]
        root = TreeNode(rootval)
        split = inorder.index(rootval)
        root.left = self.buildTree(inorder[0:split], postorder[0:split])
        root.right = self.buildTree(inorder[split+1:], postorder[split:-1], )
        return root
start_time = time.time()
app = Solution()
print(app.buildTree(inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]))

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

