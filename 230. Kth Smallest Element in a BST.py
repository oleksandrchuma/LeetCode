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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not(root):
            return -1
        visited = set()
        stack = [root]
        while stack:
            node = stack.pop()
            if node in visited:
                k -= 1
                if k == 0:
                    return node.val
            else: 
                visited.add(node)
                if node.right:
                    stack.append(node.right)
                stack.append(node)
                if node.left:
                    stack.append(node.left)
        return -1    
start_time = time.time()
t = Solution()
root = t.kthSmallest(TreeNode(1), 1)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

'''
(x+n)(n-x+1)=x(x+1) 
n2-x2+n = x2
x = sqrt((n2+n)/2)

'''