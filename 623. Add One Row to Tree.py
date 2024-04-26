from typing import List
from typing import Optional
from collections import defaultdict
import time
from collections import Counter
import math
import hashlib

 #Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        return self.addOneRowRecc(root, val, depth, True)
    def addOneRowRecc(self, root: Optional[TreeNode], val: int, depth: int, left: bool) -> Optional[TreeNode]:
        if not(root): 
            return TreeNode(val) if depth == 1 else None
        if depth > 1:
            root.left = self.addOneRowRecc(root.left, val, depth-1, True)
            root.right = self.addOneRowRecc(root.right, val, depth-1, False)
            return root
        newroot = TreeNode(val)
        if left:
            newroot.left = root 
        else:
            newroot.right = root
        return newroot
start_time = time.time()
app = Solution()
root = app.addOneRow(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3)), 8, 8)
print(root.left.val)
print(root.left.left.val)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")


