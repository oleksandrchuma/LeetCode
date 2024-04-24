import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
from queue import Queue
import math
import itertools
import heapq
from collections import Counter
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def sumRecursive(node, isLeft):
            if not(node):
                return 0
            if not(node.left) and not(node.right):
                return node.val if isLeft else 0
            return sumRecursive(node.left, True) + sumRecursive(node.right, False)
        return sumRecursive(root, False)
start_time = time.time()
t = Solution()
root = t.sumOfLeftLeaves(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4))))
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
