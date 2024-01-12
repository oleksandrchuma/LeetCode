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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        result = self.inorderTraversal(root.left)
        result.append(root.val)
        result += self.inorderTraversal(root.right)
        return result
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None: 
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)    

    def isMirroredTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None: 
            return False
        if p.val != q.val:
            return False
        return self.isMirroredTree(p.left, q.right) and self.isMirroredTree(p.left, q.right)    

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return root is None or self.isMirroredTree(root.left, root.right) 
           
start_time = time.time()
app = Solution()
tree = TreeNode(1, TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(3), TreeNode(2)))
print(app.isSymmetric(tree))

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

