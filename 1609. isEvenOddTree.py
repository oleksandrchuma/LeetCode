import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
import math
import heapq

#Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = []
        stack.append((root,1))
        iter_level = -1
        iter_val = 0
        while stack:
            node, level = stack.pop(0)
            if iter_level == level:
                if iter_level % 2 == 0 and node.val >= iter_val:
                    return False
                elif iter_level % 2 == 1 and node.val <= iter_val:
                    return False
                iter_val = node.val
            else:
                iter_level = level
                iter_val = node.val
            if (iter_level+iter_val)%2:
                return False
            if (node.left):
                stack.append((node.left, level+1))
            if (node.right):
                stack.append((node.right, level+1))
        return True
start_time = time.time()
app = Solution()
root = app.isEvenOddTree(TreeNode(1, TreeNode(4, TreeNode(5)), TreeNode(2, TreeNode(7))))
#root = app.calculateMinimumHP([[0]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

