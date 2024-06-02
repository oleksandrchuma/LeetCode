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
import numpy 
import pprint

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        if not(root): 
            return 0
        result = 0 
        if (root.left):
            result += self.distributeCoins(root.left)
            result += abs(1-root.left.val)
            root.val += root.left.val - 1
        if (root.right):
            result += self.distributeCoins(root.right)
            result += abs(1-root.right.val)
            root.val += root.right.val - 1
        return result 
start_time = time.time()
t = Solution()
root = t.distributeCoins(TreeNode(0, TreeNode(2), TreeNode(0)))
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
