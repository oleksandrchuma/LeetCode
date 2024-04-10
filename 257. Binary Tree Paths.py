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
    # Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def calc(node, path, result):
            if not(node):
                return result 
            if path != "":
                path += "->"
            path += str(node.val)
            if node.left or node.right:
                return calc(node.right, path, calc(node.left, path, result))
            result.append(path)
            return result
        return calc(root, "", [])
start_time = time.time()
t = Solution()

root = t.binaryTreePaths(TreeNode(1, TreeNode(2), TreeNode(3)))
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
