import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
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
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def depth():
            node = root
            depth = 0
            while node:
                depth += 1
                node = node.left
            return depth
        d = depth()
        if d == 0:
            return 0
        stack = [(root, 1)]
        missing = 1
        while stack:
            node, level = stack.pop()
            if level == d-1:
                if node.right:
                    break
                else: 
                    missing += 1
                if node.left:  
                    break
                else:
                    missing += 1
            else:
                if node.left:
                    stack.append((node.left, level+1))
                if node.right:
                    stack.append((node.right, level+1)) 
        return 2**d-missing    
start_time = time.time()
t = Solution()
root = t.countNodes(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3)))
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

'''
(x+n)(n-x+1)=x(x+1) 
n2-x2+n = x2
x = sqrt((n2+n)/2)

'''